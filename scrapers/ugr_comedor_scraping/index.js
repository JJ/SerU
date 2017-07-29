var request = require("request") ;
var cheerio = require("cheerio") ;
var fs = require('fs');

// url of the page we're scraping from
var url = "https://web.archive.org/web/20170114021707/http://scu.ugr.es/" ;

request(url, function (error, response, body) {
  if (!error) {

    // what to store
    var output = [] ;

    // JSON structure to store data:

    // load the entire body of the page.
    var $ = cheerio.load(body),
        // select divs which class is level1
        level1 = $('div[class=level1]') ;

    // select the main child (the first one) which contains
    // each day's menu.
    var child = level1.children().first() ;
    // for each <tr> in <table> in level1:

    var day ;


    child.children().children().each(function(i,elem){

      // in order to differenciate lines with date and lines with courses
      // we count the number of childs of each one. 2 means date (date + alergenos title)
      // 3 means courses (name, value and allergens)

      if($(this).children().length == 2){
        // this line contains the date.
        // we wrote previous json
        if (i != 0){
          output.push(day) ;
        }
        var json = {Time : "", Type : "", Data : {
          // Daily menu
          date:"",
          courses : []
        }
                   }

        day = json ;

        json.Time = new Date() ;
        json.Type = "Weekly menu" ;
        json.Data.date = $(this).children().first().text() ;

      }else{
        var coursejson = {Name : "", Value : "", Allergens : ""} ;
        var c = $(this).children().first();
        coursejson.Name =  c.text() ;
        coursejson.Value = c.next().text() ;
        coursejson.Allergens = c.next().next().text() ;
        day.Data.courses.push(coursejson) ;
      }

    });

    var file = "out/"+ new Date() + "out.json" ;
    for(index = 0 ; index < output.length ; ++index){
      fs.appendFile(file, JSON.stringify(output[index], null, 4), function(err){

                   console.log('File successfully written! - Check your project directory for the output.json file');

      })
    }



  } else {
    console.log("We’ve encountered an error: " + error);
  }
});
