
let counterElement=document.getElementById('countervalue');
console.log(counterElement);





function onIncrement() {
	let preveiousCounterValue=counterElement.textContent;
	let updateConuterValue=parseInt(preveiousCounterValue) + 1;
	console.log(updateConuterValue);
	counterElement.textContent=updateConuterValue;



	if (updateConuterValue > 0){
		counterElement.style.color = "green";
	}
	else if (updateConuterValue < 0){
		counterElement.style.color = "red"
	}

	else {
		counterElement.style.color = "black";

	}



}



function onDeccrement(){
	let preveiousCounterValue=counterElement.textContent;
	let updateConuterValue=parseInt(preveiousCounterValue) - 1;
	console.log(updateConuterValue);
	counterElement.textContent=updateConuterValue;


	if (updateConuterValue > 0){
		counterElement.style.color = "green";
	}
	else if (updateConuterValue < 0){
		counterElement.style.color = "red"
	}

	else {
		counterElement.style.color = "black";

	}








}

function onReset(){


	updateConuterValue=0;
	counterElement.textContent=updateConuterValue;

	counterElement.style.color = "black";







}