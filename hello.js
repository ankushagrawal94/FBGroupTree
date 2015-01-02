var page = require("webpage").create();
var fs = require("fs");
var homePage = "https://www.facebook.com/groups/hackathonhackers/members/";
page.settings.javascriptEnabled = false;
page.settings.loadImages = true;
page.open(homePage);
page.onLoadFinished = function(status) {
  var url = page.url;
  console.log("Status: " + status);
  console.log("Loaded: " + url);
  page.render("FacebookHH.png");

  if (url == homePage){
    page.evaluate(function() {
      var 
    })
  }

  var file = fs.open("output.htm", "w");
  file.write(page.content);
  file.close();
  phantom.exit();
};
