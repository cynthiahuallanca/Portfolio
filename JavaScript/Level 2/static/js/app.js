// from data.js
var tableData = data;

// Get a reference to the table body
var tbody = d3.select("tbody");

// To Debug. Console.log the UFO data from data.js 
//console.log(data);

// -------------- Load data into table --------------
data.forEach(function(UFO) {
   //console.log(UFO);
  var row = tbody.append("tr");
  
  Object.entries(UFO).forEach(function([key, value]) {
     //console.log(key, value);
     
     // Append a cell to the row for each value
     var cell = row.append("td");
     cell.text(value);
  });
});
// ----------------------- End ----------------------



// -------------- Filter by DateTime ----------------
// Define button 
var button = d3.select("#filter-btn-datetime");

// Function to make button filter
 button.on("click", function() {
  d3.event.preventDefault();
  console.log("Hi, a button was clicked!");
  var inputElement = d3.select("#datetime"); // Defining input element
  var inputValue = inputElement.property("value"); // Get the value property of the input element 
  console.log(inputValue); // See in the console the input value on the filter  
  // console.log(tableData); // To Debug  
  var removeBool = true;

  var filteredData = tableData.filter(record => record.datetime === inputValue);
  console.log(filteredData); // this is working. it's showing the filtered data in the log! :) yuhu

   // Debug purpose
  //console.log(filteredData); 

  // Define lenght (to use it below with if statement)
  var filteredDatalength = filteredData.length; 

  // Defining Alert when no data is found
  function myFunction() {
  alert("There's no data with your filter, Try again!");
  removeBool = false;
  }

  // Pop up alert when no data is found
  if (filteredDatalength === 0 ) {
    console.log("There's no data with your filter, Try again");
    myFunction();
  };

  // clear table to show the filtered data after
  if(removeBool === true){
  d3.select('tbody').selectAll('tr').remove();
  }
  
  // To show the filtered data
  filteredData.forEach(function(UFO) {
    //console.log(UFO);
    var row = tbody.append("tr");
    Object.entries(UFO).forEach(function([key, value]) {
      // To Debug
      //console.log(key, value);
      // Append a cell to the row for each value in the UFO report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
});
// ----------------------- End ----------------------

// ---------------- Filter by City ----------------
// Define button 
var button = d3.select("#filter-btn-city");

// Function to make button filter
 button.on("click", function() {
  d3.event.preventDefault();
  console.log("Hi, button to filter city was clicked!");
  // Defining input element
  var inputElement = d3.select("#city"); 

  // Get the value property of the input element
  var inputValue = inputElement.property("value").toLowerCase();  
  
  // See in the console the input value on the filter
  console.log(inputValue);   

  var removeBool = true;

  // Show the filtered data in the log! 
  var filteredData = tableData.filter(record => record.city === inputValue);
  console.log(filteredData); 
  
  // To Debug
  //console.log(filteredData); 

  // Define lenght (to use it below with if statement)
  var filteredDatalength = filteredData.length; 

  // Defining Alert when no data is found
  function myFunction() {
  alert("There's no data with your filter, Try again!");
  removeBool = false;
  }

  // Pop up alert when no data is found
  if (filteredDatalength === 0 ) {
    console.log("There's no data with your filter, Try again");
    myFunction();
  };

  // clear table to show the filtered data after
  if(removeBool === true){
  d3.select('tbody').selectAll('tr').remove();
  }
  
  // Show the filtered data
  filteredData.forEach(function(UFO) {
    //console.log(UFO);
    var row = tbody.append("tr");
    Object.entries(UFO).forEach(function([key, value]) {
      //console.log(key, value);
      // Append a cell to the row for each value in the UFO report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
});
// ----------------------- End ----------------------

// ---------------- Filter by State ----------------
var button = d3.select("#filter-btn-state");

// Function to make button filter
 button.on("click", function() {
  d3.event.preventDefault();
  console.log("Hi, button to filter state was clicked!");

  // Define input element
  var inputElement = d3.select("#state");
  // Get the value property of the input element
  var inputValue = inputElement.property("value").toLowerCase();  
  // see in the console the input value on the filter
  console.log(inputValue);   
  // To Debug 
  console.log(tableData);  
  
  var removeBool = true;

  // Defining filtered data 
  var filteredData = tableData.filter(record => record.state === inputValue);
  
  // Debug purpose
  //console.log(filteredData); 

  // Define lenght (to use it below with if statement)
  var filteredDatalength = filteredData.length; 

  // Defining Alert when no data is found
  function myFunction() {
  alert("There's no data with your filter, Try again!");
  removeBool = false;
  }

  // Pop up alert when no data is found
  if (filteredDatalength === 0 ) {
    console.log("There's no data with your filter, Try again");
    myFunction();
  };

  // clear table to show the filtered data after
  if(removeBool === true){
  d3.select('tbody').selectAll('tr').remove();
  }
  //TODO: improve by storing the function in a variable
  // to show the filtered data
  filteredData.forEach(function(UFO) {
    //console.log(UFO);
    var row = tbody.append("tr");
    Object.entries(UFO).forEach(function([key, value]) {
      //console.log(key, value);
      // Append a cell to the row for each value in the UFO report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
});
// ----------------------- End ----------------------

// ---------------- Filter by Shape ----------------
var button = d3.select("#filter-btn-shape");

// Function to make button filter
 button.on("click", function() {
  d3.event.preventDefault();
  console.log("Hi, button to filter shape was clicked!");
  // define input element
  var inputElement = d3.select("#shape");
   // Get the value property of the input element 
  var inputValue = inputElement.property("value").toLowerCase();
  // see in the console the input value on the filter
  console.log(inputValue);   
   // va a mostrar todos los datos, no se para que sirve aun
  console.log(tableData); 
  var removeBool = true;

  var filteredData = tableData.filter(record => record.shape === inputValue);
  console.log(filteredData);

  // Debug purpose
  //console.log(filteredData); 

  // Define lenght (to use it below with if statement)
  var filteredDatalength = filteredData.length; 

  // Defining Alert when no data is found
  function myFunction() {
  alert("There's no data with your filter, Try again!");
  removeBool = false;
  }

  // Pop up alert when no data is found
  if (filteredDatalength === 0 ) {
    console.log("There's no data with your filter, Try again");
    myFunction();
  };

  // clear table to show the filtered data after
  if(removeBool === true){
  d3.select('tbody').selectAll('tr').remove();
  }

  // to show the filtered data (tHis can be improved by defining the function in first place )
  filteredData.forEach(function(UFO) {
    //console.log(UFO);
    var row = tbody.append("tr");
    Object.entries(UFO).forEach(function([key, value]) {
      //console.log(key, value);
      // Append a cell to the row for each value in the UFO report object
      var cell = row.append("td");
      cell.text(value);
    });
  });
});
// ----------------------- End ----------------------