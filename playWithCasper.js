var casper = require('casper').create();

casper.start("http://www.facebook.com/login.php", function(response) {
    this.page.evaluate(function(a,b) {
        // login
        document.querySelector("input[name='email']").value = a
        document.querySelector("input[name='pass']").value = b;
        document.querySelector("#login_form").submit(); 
        console.log("Login submitted!");
    }, 'user','password');
}).wait(4000, function(){
    this.capture('imgRepeats/'+'ihateads@yahoo.com'+'_login.png');
})

casper.thenOpen('https://www.facebook.com/groups/hackathonhackers/members/?order=alphabetical', function() {
    this.echo(this.getTitle());
    this.capture('imgRepeats/'+'hackathonhackers.png');
    if (this.exists('a.pam.uiBoxLightblue.uiMorePagerPrimary')) {
        this.echo('the see more button exists');
        this.mouseEvent('click', 'a.pam.uiBoxLightblue.uiMorePagerPrimary');
    }
    else{
      console.log('the see more button does not exist :[ ');
    }
}).wait(4000);

var j = 0
for( i = 0; i < 150; i++) {
  casper.then(function() {
    console.log("next then :D");
    this.capture('imgRepeats/'+'hackathonhackers' + j++ + '.png');
    if (this.exists('a.pam.uiBoxLightblue.uiMorePagerPrimary')) {
          this.echo('the heading exists');
          this.mouseEvent('click', 'a.pam.uiBoxLightblue.uiMorePagerPrimary');
      }
      else{
        console.log('does not exist :[ ');
      }
  }).wait(4000);

  casper.then(function() {
    console.log(this.getHTML());
  });
}





































/*
casper.then(function() {
  console.log("Another then :D");
  this.capture('img/'+'hackathonhackers5.png');
  var js = this.evaluate(function() {
    var items = document.getElementsByClassName('div._8u._42ef');
    console.log(items.length);
    for (var i = 0; i < items.length; i++) {
      console.log(items[i]);
    }
    return document; 
  }); 
  //this.echo(js.all[1]);
  
  //console.log(items); 
  //console.log(this.getHTML());
  console.log(this.getHTML('div._17tq'));
  console.log(this.getHTML('div._17tq'));
  console.log(this.getHTML('div._8u._42ef'));
  console.log(this.getHTML('div._8u._42ef'));
  console.log(this.getHTML('div._8u._42ef'));
  console.log(this.getHTML('div.clearfix'));
  console.log(this.getHTML('div.clearfix'));
  console.log(this.getHTML('div.clearfix'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  console.log(this.getHTML('div.fsm.fwn.fcg'));
  //console.log(this.getHTML('div.8u._42ef'));
  //var el = document.createElement('div');
  //el.innerHTML = this.getHTML('div.8u._42ef');
  //console.log(el.getElementsByTagName( 'a' ));
  //console.log("\n\n" + el);
});*/

casper.run();
