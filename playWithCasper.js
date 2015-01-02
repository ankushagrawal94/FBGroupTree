var casper = require('casper').create();

casper.start("http://www.facebook.com/login.php", function(response) {
    this.page.evaluate(function(a,b) {
        // login
        document.querySelector("input[name='email']").value = a
        document.querySelector("input[name='pass']").value = b;
        document.querySelector("#login_form").submit(); 
        console.log("Login submitted!");
    }, 'user_email','user_password');
}).wait(1000, function(){
    //this.capture('img/'+'ihateads@yahoo.com'+'_login.png');
})

casper.thenOpen('https://www.facebook.com/groups/hackathonhackers/members/?order=alphabetical', function() {
    this.echo(this.getTitle());
    this.capture('img/'+'hackathonhackers.png');
    this.mouseEvent('click', 'a.pam.uiBoxLightblue.uiMorePagerPrimary');
    this.wait(10000);
});

casper.then(function() {
  console.log("next then :D");
  this.capture('img/'+'hackathonhackers2.png');
  if (this.exists('a.pam.uiBoxLightblue.uiMorePagerPrimary')) {
        this.echo('the heading exists');
    }
    else{
      console.log('does not exist :[ ');
    }
})


casper.run();