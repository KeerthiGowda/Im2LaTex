var sketchProc=function(processingInstance){ with (processingInstance){
size(800, 800); 


frameRate(200);

var clicked = 0;
var clear = 0;
var submit = 0;

mouseClicked = function() {
    if(mouseX > 20 && mouseX < 110){
        if(mouseY > 750 && mouseY < 790){
            clear = 1;
            clicked = 0;
        }
    } 
     if(mouseX > 740 && mouseX < 790){
        if(mouseY > 750 && mouseY < 790){
            submit = 1;
        }
    } 
};

var mousePressed = function(){
    if(mouseY < 750){
        clicked = 1;
    }
};

var mouseReleased = function(){
    clicked = 0;
};

var displayCustomText = function(a, x, y, font){
    var f = createFont("Comic Sans");
    textFont(f, font);
    text(a, x, y);
};

var initialized = 0;
var initialize = function(){
      initialized = 1;
      strokeWeight(5);
      rect(0,0,800,800);
      noStroke();
      fill(92,58,6);
      rect(0, 740, 800, 60);      

      fill(255,100,100,100);
      rect(20, 750, 90, 40,20);
      rect(740, 750, 50, 40,20);
      fill(230,212,9);
      displayCustomText("Clear", 30, 780, 30);
      text("ok", 750, 780);
      line(0, 740, 800, 740);
      
      noStroke();
      fill(92,58,6);
      rect(0,0,800, 120);
      fill(230, 212, 9);
      displayCustomText("Im2Latex", 300, 50, 40);
      displayCustomText("What's in your mind today!!", 50, 100, 60);
		
};
 
var draw = function() {
    if(initialized === 0){
	background(255, 255, 255);
        initialize();
    }
    
    if(clicked === 1){
        stroke(0, 0, 0);
        fill(0, 0, 0);
	strokeWeight(5);
	if(mouseY>130 & pmouseY > 130){
		if(mouseY<730 & pmouseY <730){   
		  line(pmouseX, pmouseY,mouseX, mouseY);
		}
	}
    }
    if(clear === 1){
        fill(255, 255, 255);
		noStroke();
        rect(0,120,800, 620);
        clear = 0;
    }
    if(submit === 1){
        var canvas = document.getElementById("mycanvas");
	var img    = canvas.toDataURL("image/png");
	document.write('<img src="'+img+'"/>');
    }
};


}};

