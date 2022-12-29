"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
// Helper functions
// function clone(val: any) {
//   return JSON.parse(JSON.stringify(val))
// }
function clone(val) {
    const type = typeof val;
    if (val === null) {
        return null;
    }
    else if (type === 'undefined' || type === 'number' ||
        type === 'string' || type === 'boolean') {
        return val;
    }
    else if (type === 'object') {
        if (val instanceof Array) {
            return val.map(x => clone(x));
        }
        else if (val instanceof Uint8Array) {
            return new Uint8Array(val);
        }
        else {
            let o = {};
            for (const key in val) {
                o[key] = clone(val[key]);
            }
            return o;
        }
    }
    throw 'unknown';
}
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}
// Runs this code if the plugin is run in Figma
if (figma.editorType === 'figma') {
    // This plugin will open a window to prompt the user to enter a number, and
    // it will then create that many rectangles on the screen.
    // This shows the HTML page in "ui.html".
    figma.showUI(__html__);
    figma.ui.onmessage = (msg) => __awaiter(void 0, void 0, void 0, function* () {
        if (msg.type === 'create-shapes') {
            const nodes = [];
            for (let i = 0; i < msg.count; i++) {
                const rect = figma.createRectangle();
                rect.x = i * 150;
                rect.fills = [{ type: 'SOLID', color: { r: 1, g: 0.5, b: 0 } }];
                figma.currentPage.appendChild(rect);
                nodes.push(rect);
            }
            figma.currentPage.selection = nodes;
            figma.viewport.scrollAndZoomIntoView(nodes);
        }
        else if (msg.type === 'send_commands') {
            console.log("Get message from front end!!");
            console.log(msg);
            // TODO: use a dict to store id like '1:1317'
            let title_node = figma.getNodeById('1:1317');
            if (title_node) {
                yield figma.loadFontAsync(title_node.fontName);
                title_node.characters = msg.result_str.toUpperCase();
            }
            else {
                console.warn("Bad title node id, please set it manually");
            }
            // Simple create text test
            // const text = figma.createText()
            // // Make sure the new text node is visible where we're currently looking
            // text.x = figma.viewport.center.x
            // text.y = figma.viewport.center.y
            // await figma.loadFontAsync(text.fontName as FontName)
            // text.characters = msg.result_str
            // // text.characters = await msg.result_str
        }
        else if (msg.type === 'gen_text') {
            console.log("Get message from gen_text!!");
            let title_node = figma.getNodeById('1:1325');
            if (title_node) {
                yield figma.loadFontAsync(title_node.fontName);
                title_node.characters = msg.result_str;
                // title_node.characters = capitalizeFirstLetter(msg.result_str)
            }
            else {
                console.warn("Bad title node id, please set it manually");
            }
        }
        else if (msg.type == 'gen_image') {
            console.log("gen_image!!!!!!!!!!!!!");
            fetch(msg.img_url)
                .then(response => response.arrayBuffer())
                .then((image) => {
                // const newFills = []
                console.log(image);
                let img_data = new Uint8Array(image);
                let figma_image = figma.createImage(img_data);
                console.log('figma_image', figma_image);
                // figma.getNodeById('1:7').fills = figma_image
                let background_image_node = figma.getNodeById('1:7');
                if (background_image_node) {
                    background_image_node.fills = [
                        {
                            blendMode: 'NORMAL',
                            imageHash: figma_image.hash,
                            type: 'IMAGE',
                            visible: true,
                            scaleMode: 'FILL',
                        },
                    ];
                }
                else {
                    console.warn("Bad title node id, please set it manually");
                }
            });
        }
        else if (msg.type === 'gen_free_text') {
            console.log("Get message from gen_free_text!!");
            // console.log(figma.currentPage.selection)
            var title_node = figma.currentPage.selection[0];
            console.log(title_node);
            if (title_node) {
                console.log('title_node.type', title_node.type);
                if (title_node) {
                    yield figma.loadFontAsync(title_node.fontName);
                    title_node.characters = msg.result_str;
                    // title_node.characters = capitalizeFirstLetter(msg.result_str)
                }
                else {
                    console.warn("Selected element was not text!");
                }
            }
            else {
                console.warn("No item was selected");
            }
        }
        // figma.closePlugin()
    });
    // Calls to "parent.postMessage" from within the HTML page will trigger this
    // callback. The callback will be passed the "pluginMessage" property of the
    // posted message.
    // Make sure to close the plugin when you're done. Otherwise the plugin will
    // keep running, which shows the cancel button at the bottom of the screen.
    // figma.closePlugin();
    // If the plugins isn't run in Figma, run this code
}
else {
    // This plugin will open a window to prompt the user to enter a number, and
    // it will then create that many shapes and connectors on the screen.
    // This shows the HTML page in "ui.html".
    figma.showUI(__html__);
    // Calls to "parent.postMessage" from within the HTML page will trigger this
    // callback. The callback will be passed the "pluginMessage" property of the
    // posted message.
    figma.ui.onmessage = msg => {
        // One way of distinguishing between different types of messages sent from
        // your HTML page is to use an object with a "type" property like this.
        if (msg.type === 'create-shapes') {
            const numberOfShapes = msg.count;
            const nodes = [];
            for (let i = 0; i < numberOfShapes; i++) {
                const shape = figma.createShapeWithText();
                // You can set shapeType to one of: 'SQUARE' | 'ELLIPSE' | 'ROUNDED_RECTANGLE' | 'DIAMOND' | 'TRIANGLE_UP' | 'TRIANGLE_DOWN' | 'PARALLELOGRAM_RIGHT' | 'PARALLELOGRAM_LEFT'
                shape.shapeType = 'ROUNDED_RECTANGLE';
                shape.x = i * (shape.width + 200);
                shape.fills = [{ type: 'SOLID', color: { r: 1, g: 0.5, b: 0 } }];
                figma.currentPage.appendChild(shape);
                nodes.push(shape);
            }
            ;
            for (let i = 0; i < (numberOfShapes - 1); i++) {
                const connector = figma.createConnector();
                connector.strokeWeight = 8;
                connector.connectorStart = {
                    endpointNodeId: nodes[i].id,
                    magnet: 'AUTO',
                };
                connector.connectorEnd = {
                    endpointNodeId: nodes[i + 1].id,
                    magnet: 'AUTO',
                };
            }
            ;
            figma.currentPage.selection = nodes;
            figma.viewport.scrollAndZoomIntoView(nodes);
        }
        // Make sure to close the plugin when you're done. Otherwise the plugin will
        // keep running, which shows the cancel button at the bottom of the screen.
        figma.closePlugin();
    };
}
;
