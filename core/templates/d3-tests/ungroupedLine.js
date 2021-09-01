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
  const dataset = await d3.csv("./data.csv") //, function(csv) {
    //csv['InvoiceDate'] = format(csv['InvoiceDate'])})
  console.log("Data Loaded: ", dataset.slice(0,10))

  const format = d3.timeFormat("%M/%d/%Y %H:%m")
  const parseDate = d3.timeParse('%M/%d/%Y %H:%m')
  const xAccessor = d => format(parseDate(d.InvoiceDate))
  const yAccessor = d => parseInt(d.UnitPrice)

  // Dimensions
  let dimensions = {
      width: 1680,
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
                 ,`translate(${dimensions.margin}, ${dimensions.margin})`) // center container
  
  console.log("Container Loaded")

  // Scales
  const yScale = d3.scaleLinear()
    .domain(d3.extent(dataset, yAccessor)) //.slice(0,10000)
    .range([dimensions.ctrHeight, 0])
    .nice()

  const xScale = d3.scaleUtc()
    .domain(d3.extent(dataset.slice(0,10000), xAccessor))
    .range([0, dimensions.ctrWidth])    
  
  console.log(xScale(xAccessor(dataset[0])))
  console.log(xAccessor(dataset[0]))
  console.log("Without formatting: ", dataset[0].InvoiceDate)
  console.log("Scaled Loaded")

  
  const lineGenerator = d3.line()
    .x( (d) => xScale(xAccessor(d)))
    .y( (d) => yScale(yAccessor(d)))

  //console.log(lineGenerator(dataset))
  ctr.append('path')
    .datum(dataset)
    .attr('d', lineGenerator)
    .attr('fill', 'none')
    .attr('stroke', '#30475e')
    .attr('stroke-width', 2)
  /*   
  ctr.selectAll('circle')
    .data(dataset)
    .join('circle')
    .attr('cx', d => xScale(xAccessor(d)))
    .attr('cy', d => yScale(yAccessor(d)))
    //.attr('r', 5)
    .attr('b', 2)
    .attr('fill', 'black')
  */

}


draw()
