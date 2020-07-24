function uncheck(soundCheck) {
    document.getElementById(soundCheck).checked = false;
}


function changeStyle(soundCheck, checkedLabel, uncheckedLabel){
		if (document.getElementById(soundCheck).checked){
			console.log("checked");
			document.getElementById(checkedLabel).style.display = "block";
			document.getElementById(uncheckedLabel).style.display = "none";
		}
		else{
			console.log("unchecked");
			document.getElementById(checkedLabel).style.display = "none";
			document.getElementById(uncheckedLabel).style.display = "block";
		}
}

for (let item of document.getElementsByClassName("soundLabel")) {
    item.style.display = "none";
}

var mySound = undefined;
var turned = false;
var paused = false;
	
soundManager.setup({
	url: "/swf/"
	});

function PlaySound(soundUrl, soundCheck, checkedLabel, uncheckedLabel)
{
	changeStyle(soundCheck, checkedLabel, uncheckedLabel);

	if (!mySound || mySound.url !== soundUrl){
		if (mySound){
			turned = false;
			paused = false;
			
			mySound.stop();
		}
				
		mySound = soundManager.createSound({
				url: soundUrl,
				onfinish: function(){
					turned = false;
					paused = false;
					uncheck(soundCheck);
					changeStyle(soundCheck, checkedLabel, uncheckedLabel);
				},
				onstop: function(){
					turned = false;
					paused = false;
					uncheck(soundCheck);
					changeStyle(soundCheck, checkedLabel, uncheckedLabel);
				}
				
			});
	}
	if (!turned && !paused){
		turned = true;
		mySound.play();
		return;
	}
	if (!paused)
	{
		paused = true;
		mySound.pause();
		return;
	}

	if (paused)
	{
		paused = false;
		mySound.resume();
		return;
	}
}


