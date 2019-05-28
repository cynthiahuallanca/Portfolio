
    ////////////////BAR
    function draw(data) {
      
      /*
        D3.js setup code
      */
      console.log('DATA');
      console.log(data);
      // data.forEach(d =>{
      //   console.log(d.issue_type);
      // });
          "use strict";
          var margin = 15,
              width = 1500 - margin,
              height = 950 - margin;

          var svg = d3.select("body")
            .append("svg")
              .attr("width", width + margin)
              .attr("height", height + margin)
            .append('g')
                .attr('class','chart');

      /*
        Dimple.js Chart construction code
      */

          var myChart = new dimple.chart(svg, data);
          var x = myChart.addCategoryAxis("x", ["city", "case_owner"]); 
          var y = myChart.addMeasureAxis("y", "efficiency");
          y.tickFormat = "%";
          y.ticks = 5;
          myChart.addSeries("issue_type", dimple.plot.bar);
          myChart.addLegend(900, 200, 510, 1000, "right");
          myChart.draw();
        };

        d3.json("/efficiency-data", draw);