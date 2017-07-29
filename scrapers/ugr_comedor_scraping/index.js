var request = require("request") ;
var cheerio = require("cheerio") ;

// url of the page we're scraping from
var url = "https://web.archive.org/web/20170114021707/http://scu.ugr.es/" ;

request(url, function (error, response, body) {
  if (!error) {

    // what to store
    var output = [] ;

    // JSON structure to store data:

    var json = {"Time" : "", "Type" : "", "Data" : {
      // Daily menu
      "date":"",
      "courses" :
      [{"Name" : "", "Value" : "", "Allergens" : ""}]
    }
               }

    json.Time = new Date() ;
    json.Type = "Weekly menu" ;


    // load the entire body of the page.
    var $ = cheerio.load(body),
        // select divs which class is level1
        level1 = $('div[class=level1]') ;

    // select the main child (the first one) which contains
    // each day's menu.
    var child = level1.children().first() ;
    // for each <tr> in <table> in level1:
    var j = 0 ;
    child.children().children().each(function(i,elem){
      console.log("\n"+$(this).children().length) ;

      // in order to differenciate lines with date and lines with courses
      // we count the number of childs of each one. 2 means date (date + alergenos title)
      // 3 means courses (name, value and allergens)

      if($(this).children().length == 2){
        // this line contains the date.
        // we wrote previous json
        if (i != 0){
          output[i]  = json ;
          i++ ;
          j = 0 ;
        }
        json.Data.date = $(this).children().first().text() ;
      }else{
        var c = $(this).children().first();
        json.Data.courses[j++].Name =  c.text() ;
        json.Data.courses[j++].Value = c.next().text() ;
        json.Data.courses[j++].Allergens = c.next().next().text() ;
      }

    });

    console.log(json) ;

  } else {
    console.log("We’ve encountered an error: " + error);
  }
});
