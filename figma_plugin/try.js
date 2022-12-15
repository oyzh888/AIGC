for (const node of figma.currentPage.selection) {
    console.log(node)
    node.characters = 'OYZH new test str'
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