// @TODO: add state abbreviation into each circle// do an overlay 


function makeResponsive() {
  var svgArea = d3.select("body").select("svg");

  if (!svgArea.empty()) {
    svgArea.remove();
  }


var svgWidth = window.innerWidth;
var svgHeight = window.innerHeight;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};


var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create an SVG wrapper, append an SVG group that will hold our chart, and shift the latter by left and top margins.
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);


// Import Data
d3.csv("assets/data/data.csv")
  .then(function(DData) {

    console.log(DData);

    
    // Step 1: Parse Data/Cast as numbers
    // ==============================
    DData.forEach(function(data) {
      data.age = +data.age;
      data.smokes = +data.smokes;
      //data.avg = createPercent(data.smokes/data.age);
    });


    // Step 2: Create scale functions
    // ==============================
    var xLinearScale = d3.scaleLinear()
      .domain([30, d3.max(DData, d => d.age)])
      .range([0, width]);

    var yLinearScale = d3.scaleLinear()
      .domain([6, d3.max(DData, d => d.smokes)])
      .range([height, 0]);

    // Step 3: Create axis functions
    // ==============================
    var bottomAxis = d3.axisBottom(xLinearScale);
    var leftAxis = d3.axisLeft(yLinearScale);

    // Step 4: Append Axes to the chart
    // ==============================
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .call(bottomAxis);

    chartGroup.append("g")
      .call(leftAxis);


    // Step 5: Create Circles //TODO. add another circel that overlap this with the abbreviation of the states 
    // ==============================
    var circlesGroup = chartGroup.selectAll("circle")
    .data(DData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.age))
    .attr("cy", d => yLinearScale(d.smokes))
    .attr("r", "15")
    .attr("fill", "gold")
    .attr("stroke", "black")
    .attr("stroke-width", "1")
    .attr("opacity", ".85");
  
    // Adding state abbreviation to each circle
    var textGroup = chartGroup.selectAll("text")
        .data(DData)
        .enter()
        .append("text")
        .text(d => d.abbr)
        .attr("x", d => xLinearScale(d.age))
        .attr("y", d => yLinearScale(d.smokes)+4) 
        .attr("color","black")
        .attr("text-anchor", "middle")
        .classed("StateAbbr", true)
        
    // Step 6: Initialize tool tip
    // ==============================
    var toolTip = d3.tip()
      .attr("class", "tooltip")
      .offset([80, -60])
      .html(function(d) {
        return (`${d.state}<br>Age: ${d.age}<br>Smokes: ${d.smokes}`);
      });

    // Step 7: Create tooltip in the chart
    // ==============================
    chartGroup.call(toolTip);

    // Step 8: Create event listeners to display and hide the tooltip
    // ==============================
    circlesGroup.on("mousemove", function(data) {
      toolTip.show(data, this);
      circlesGroup = renderCircles_y(circlesGroup, yLinearScale, chosenYAxis);
      circlesText = renderCirclesText_y(circlesText, yLinearScale, chosenYAxis);
    })

    //To display tooltip when mouse is over state abbrviation too. It's not really necessarry because it's already in the circles but it makes the use interfase better 
    textGroup.on("mousemove", function(data) {
      toolTip.show(data, this);
      circlesGroup = renderCircles_y(circlesGroup, yLinearScale, chosenYAxis);
      circlesText = renderCirclesText_y(circlesText, yLinearScale, chosenYAxis);
    })
      // onmouseout event
      .on("mouseout", function(data, index) {
        toolTip.hide(data);
      });

    // Create axes labels
    chartGroup.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left + 40)
      .attr("x", 0 - (height / 2))
      .attr("dy", "1em")
      .attr("class", "axisText")
      .text("Smokes");

    chartGroup.append("text")
      .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
      .attr("class", "axisText")
      .text("Age");
  });

}
  makeResponsive();

  // Event listener for window resize.
// When the browser window is resized, makeResponsive() is called.
d3.select(window).on("resize", makeResponsive);
