
async function draw() {
  
  // Data
  // const dataset = await d3.csv("./data.csv") 
  // date format 12/1/2010 11:33
  // dataset.forEach(function(d) {d.InvoiceDate = parseDate(d.InvoiceDate)})
  const dataset = await d3.csv("./data.csv") //, function(csv) {
    //csv['InvoiceDate'] = format(csv['InvoiceDate'])})

  const formatA = d3.timeFormat("%M/%d/%Y")
  const parseDateA = d3.timeParse('%M/%d/%Y %H:%m')  
  const formatB = d3.timeFormat("%M/%d/%Y")
  const parseDateB = d3.timeParse('%M/%d/%Y')

  // for dates on rollup array
  const xAccessor = d => parseDateB(d[0]) // format(parseDate(d.InvoiceDate))
  // for price on rollup array
  const yAccessor = d => d[1]//parseInt(d.UnitPrice)
  // nested array for graphing
  const groupSum = d3.rollups(dataset, v => d3.sum(v, d => d.UnitPrice), d => formatA(parseDateA(d.InvoiceDate)))
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
    .domain(d3.extent(groupSum, yAccessor)) // dataset.slice(0,10000), yAccessor)) //.slice(0,10000)
    .range([dimensions.ctrHeight, 0])
    .nice()
  console.log("yScale: ", yScale.domain())

  const xScale = d3.scaleTime()
    .domain(d3.extent(groupSum, xAccessor)) // dataset.slice(0,10000), xAccessor))
    .range([0, dimensions.ctrWidth])    

  // console.log("xScale: ", xScale.domain())
  // console.log("With xAccessor: ", (xAccessor(groupSum[0])))
  // console.log("Without xAccessor: ", groupSum[0][0])
  //with the formatting it does not work
  //console.log("xScale: ", xScale)
  //console.log("With yAccessor: ", (yAccessor(groupSum[0])))
  //console.log("Without formatting: ", groupSum[0].InvoiceDate)
  console.log("Scales Loaded")
  
  const lineGenerator = d3.line()
    .x( d => xAccessor(d))
    .y( d => yAccessor(d))
  // Axis
  const yAxis = d3.axisLeft(yScale)
    .tickFormat((d) => `$${d}`)
  // append scale to graph
  ctr.append('g')
    .call(yAxis)
  
  const xAxis = d3.axisBottom(xScale)
  // append scale
  ctr.append('g')
    .style('transform', `translateY(${dimensions.ctrHeight}px)`)
    .call(xAxis)

  console.log("Line: ", lineGenerator(groupSum))
  ctr.append('path')
    .datum(groupSum.slice(0,10000))
    .attr('d', lineGenerator)
    .attr('fill', 'none')
    .attr('stroke', 'steelblue')
    .attr('stroke-width', 1.5)/*
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
      // Tooltip
  ctr.append('rect')
    .attr('width', dimensions.ctrWidth)
    .attr('height', dimensions.ctrHeight)
    .style('opacity', 0)
    })*/




}


draw().then(response => {
  console.log("Response: ", response)
}).catch(e => {
  console.log("Error: ",e)
})
