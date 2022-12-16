// Hint:
//TODO: UtoDian/Github/plugin-samples/metacards

// res = fetch('https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495')
// .then(response => response.blob())
res = fetch('https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495')
.then(response => response.arrayBuffer())
res.then(
  (image) => {
    // const newFills = []
    console.log(image)
    let img_data = new Uint8Array(image)
    let figma_image = figma.createImage(img_data)
    console.log('figma_image', figma_image)
    figma.getNodeById('1:7').fills = figma_image
  }
)

// const figma_image = figma.createImage(image)
new Uint8Array(response.arrayBuffer())
let img_node = figma.getNodeById('1:7')




res = fetch('https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495')
res = res.then(response => response)

fetch('https://lexica-serve-encoded-images.sharif.workers.dev/md/003cc1f0-e52a-400f-808f-358183156495')
.then(response => response.blob())
.then(image => console.log(image))


// Modify
file.getBytesAsync().then(bytes => {
  const image = figma.createImage(bytes)

let file_path = "/Users/ouyangzhihao/Library/Mobile\ Documents/com~apple~CloudDocs/PycharmProjects/UtoDian/Github/AIGC/python_backend/img_folder/apple/0.jpg"
figma.file.getBytesAsync.getBytesAsync(file_path)

const colors = figma.currentPage.findAll(n => n.name === "as")

figma.currentPage.selection = [figma.getNodeById('1:1317'), figma.getNodeById('1:1316')]

figma.getNodeById('1:1317').characters = 'AItist'
figma.getNodeById('1:1317').id

figma.loadFontAsync({ family: "Iowan Old Style", style: "Titling" })
figma.getNodeById('1:1317').characters = 'OYZH'

var node = figma.getNodeById('1:1317');

const node = figma.getNodeById(nodeId);

let select_count = 0
for (const node of figma.currentPage.selection) {
  select_count += 1
  console.log(node)
  // if ("opacity" in node) {
  //   node.opacity *= 0.5
  // }
}
console.log(select_count)

figma.currentPage.selection = [figma.getNodeById('1:2630')]

// This plugin counts the number of layers, ignoring instance sublayers,
// in the document
let count = 0
function traverse(node) {
  if ("children" in node) {
    console.log(node)
    count++
    if (node.type !== "INSTANCE") {
      for (const child of node.children) {
        traverse(child)
      }
    }
  }
}
traverse(figma.root) // start the traversal at the root
console.log(count)

traverse(figma.currentPage)

let nodeId='1:2'
nodeId = '104:22'
traverse(figma.getNodeById(nodeId))

// Finds all empty frame nodes
const nodes = node.findAll(node => {
  return node.type === "FRAME" && node.children.length === 0
})


// Finds all component and component set nodes
const nodes = figma.root.findAllWithCriteria({
  types: ['COMPONENT', 'COMPONENT_SET']
})

for (const node of figma.currentPage) {
  console.log(node)
  // node.characters = 'OYZH new test str'
  // if ("opacity" in node) {
  //   node.opacity *= 0.5
  // }
}

for (const node of figma.currentPage.selection) {
    console.log(node)
    // node.characters = 'OYZH new test str'
    // if ("opacity" in node) {
    //   node.opacity *= 0.5
    // }
}
figma.closePlugin()


for (const node of figma.currentPage.selection) {
    if ("opacity" in node) {
      node.opacity *= 0.5
    }
  }
  figma.closePlugin()