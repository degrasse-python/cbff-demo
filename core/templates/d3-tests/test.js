/*

=========================================================
* New Bee -  Dashboard
=========================================================


=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. Please contact us to request a removal. Contact us if you want to remove it.

*/

async function draw() {
  // Data
  // const dataset = await d3.csv("./data.csv") 
  // date format 12/1/2010 11:33
  // dataset.forEach(function(d) {d.InvoiceDate = parseDate(d.InvoiceDate)})
  const dataset = await d3.csv("./data.csv", function(csv) {
  const format = d3.timeFormat("%m/%d/%Y %H:%M")

  csv['InvoiceDate'] = format(csv['InvoiceDate'])})
  
  console.log("Data Loaded")

  const parseDate = d3.timeParse('%m/%d/%Y %H:%m')
  const xAccessor = d => parseDate(d.InvoiceDate)
  const yAccessor = d => d.UnitPrice
  // Dimensions
  let dimensions = {
      width: 800,
      height: 800,
      margin: 50
  }
  dimensions.ctrWidth = dimensions.width - dimensions.margin * 2
  dimensions.ctrHeight = dimensions.height - dimensions.margin * 2

  // Draw image
  const svg = d3.select('#chart')
      .append('svg')
      .attr('width', dimensions.width)
      .attr('height', dimensions.height)
  console.log("SVG Loaded")

  // add margins
  const ctr = svg.append('g') // create g container
                 .attr('transform' 
                 ,`translate(${dimensions.margin}, ${dimensions.margin})`)// center container
  
  console.log("Container Loaded")

  // Scales
  const yScale = d3.scaleLinear()
    .domain(d3.extent(dataset, yAccessor))
    .range([dimensions.ctrHeight, 0])
    .nice()
  const xScale = d3.scaleTime()
    .domain(d3.extent(dataset, xAccessor))
    .range([0, dimensions.ctr])    
  
  console.log("Scaled Loaded")

  // 
  const lineGenerator = d3.line()
    .x((d) => xScale(xAccessor(d)))
    .y((d) => yScale(yAccessor(d)))

  console.log(lineGenerator(dataset))
  ctr.append('path')
    .datum(dataset)
    .attr('d', lineGenerator)
    .attr('fill', 'none')
    .attr('stroke', '#30475e')
    .attr('stroke-width', 2)

}


draw()
