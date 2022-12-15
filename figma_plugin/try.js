// Modify

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