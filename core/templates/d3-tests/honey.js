
async function draw() {
  
  // Data
  // const dataset = await d3.csv("./data.csv") 
  // date format 12/1/2010 11:33
  // dataset.forEach(function(d) {d.InvoiceDate = parseDate(d.InvoiceDate)})
  const dataset = await d3.csv("./data.csv") //, function(csv) {
    //csv['InvoiceDate'] = format(csv['InvoiceDate'])})

  const format = d3.timeFormat("%M/%d/%Y")
  const parseDate = d3.timeParse('%M/%d/%Y %H:%m')
  // for dates on rollup array
  const xAccessor = d => d[0]// format(parseDate(d.InvoiceDate))
  // for price on rollup array
  const yAccessor = d => d[1]//parseInt(d.UnitPrice)
  // nested array for graphing
  const groupSum = d3.rollups(dataset, v => d3.sum(v, d => d.UnitPrice), d => format(parseDate(d.InvoiceDate)))
  console.log("Data Loaded: ", groupSum[0])
  // Dimensions
  let dimensions = {
      width: 1680,
      height: 800,
      margin: 100
  }
  dimensions.ctrWidth = dimensions.width - dimensions.margin * 2
  dimensions.ctrHeight = dimensions.height - dimensions.margin * 2

  // init svg image
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

  // tooltip
  const tooltip = d3.select('#tooltip')
  const tooltipDot = ctr.append('circle')
    .attr('r', 5)
    .attr('fill', '#fc8781')
    .attr('stroke', 'black')
    .attr('stroke-width', 2)
    .style('opacity', 0)
    .style('pointer-events', 'none')

    
  // Scales
  const yScale = d3.scaleLinear()
    .domain(d3.extent(groupSum.slice(0,10000)), yAccessor) // dataset.slice(0,10000), yAccessor)) //.slice(0,10000)
    .range([dimensions.ctrHeight, 0])
    .nice()

  const xScale = d3.scaleUtc()
    .domain(d3.extent(groupSum.slice(0,10000)), xAccessor) // dataset.slice(0,10000), xAccessor))
    .range([0, dimensions.ctrWidth])    
  
    // with the formatting it does not work
  //console.log("With xScale: ", xScale(xAccessor(dataset[0])))
  //console.log("With xAccessor: ", (xAccessor(dataset[0])))
  //console.log("Without formatting: ", groupSum[0].InvoiceDate)
  console.log("Scaled Loaded")

  const lineGenerator = d3.line()
    .x( (d) => xScale(xAccessor(d)))
    .y( (d) => yScale(yAccessor(d)))

  //console.log(lineGenerator(dataset))
  ctr.append('path')
    .datum(groupSum.slice(0,10000))
    .attr('d', lineGenerator)
    .attr('fill', 'none')
    .attr('stroke', '#30475e')
    .attr('stroke-width', 2)/*
    .on('touchmouse mousemove', function(event) {
      const mousePos = d3.pointer(event, this)
      const date = xScale.invert(mousePos[0])

      // Bisector - left, center, right
      const bisector = d3.bisect(xAccessor).left
      const index = bisector(groupSum, date)
      const unitPrice = groupSum[index - 1]

      tooltipDot.style('opacity', 1)
        .attr('cx', xScale(xAccessor(unitPrice)))
        .attr('cy', yScale(yAccessor(unitPrice)))
        .raise()

    })
    .on('mouseleave', function (event) {
      
    })*/

  // Axis
  const yAxis = d3.axisLeft(yScale)
    .tickFormat((d) => `$${d}`)
  ctr.append('g')
    .call(yAxis)

  const xAxis = d3.axisBottom(xScale)
  ctr.append('g')
    .style('transform', `translateY(${dimensions.ctrHeight}px)`)
    .call(xAxis)

  // Tooltip
  ctr.append('rect')
    .attr('width', dimensions.ctrWidth)
    .attr('height', dimensions.ctrHeight)
    .style('opacity', 0)

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


draw().then(response => {
  console.log("Response: ", response)
}).catch(e => {
  console.log("Error: ",e)
})
