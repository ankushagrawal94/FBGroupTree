var casper = require('casper').create();

casper.start("http://www.facebook.com/login.php", function(response) {
    this.page.evaluate(function(a,b) {
        // login
        document.querySelector("input[name='email']").value = a
        document.querySelector("input[name='pass']").value = b;
        document.querySelector("#login_form").submit(); 
        console.log("Login submitted!");
    }, 'user-email','user-password');
}).wait(4000, function(){
    this.capture('imgTwoLetter/'+'ihateads@yahoo.com'+'_login.png');
})

var alphabet = "abcdefghijklmnopqrstuvwxyz";
twoLetter = []
for( i = 0; i < alphabet.length; i++) {
  for( j = 0; j < alphabet.length; j++){
    twoLetter.push(alphabet[i] + alphabet[j]);
  }
}

console.log(twoLetter.length)

var j = 0;
for (i = 0; i < twoLetter.length; i++){
  casper.then(function() {
    this.open('https://www.facebook.com/groups/1506039289667163/members/?order=alphabetical&member_query='+twoLetter[j++]).then(function() {
      var page_title = this.getTitle();
      this.echo(page_title);
      this.capture('img/'+ page_title + twoLetter[j] + '.png');
    })
  })
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
