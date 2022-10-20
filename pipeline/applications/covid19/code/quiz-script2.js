var currentQuestion = 0;
var score = 0;
var RI = 0;
var totQuestions = questions.length;

var container = document.getElementById('quizContainer');
var questionEl = document.getElementById('question');
var opt1 = document.getElementById('opt1');
var opt2 = document.getElementById('opt2');
var opt3 = document.getElementById('opt3');
var opt4 = document.getElementById('opt4');
var nextButton = document.getElementById('nextButton');
var resultCont = document.getElementById('result');
var nexttest   =  document.getElementById('nextButton');


var interpretationCont = document.getElementById('interpretation');
var questionEll = document.getElementById('question1');


function parseURLParams(url) {
    var queryStart = url.indexOf("?") + 1,
        queryEnd   = url.indexOf("#") + 1 || url.length + 1,
        query = url.slice(queryStart, queryEnd - 1),
        pairs = query.replace(/\+/g, " ").split("&"),
        parms = {}, i, n, v, nv;

    if (query === url || query === "") return;

    for (i = 0; i < pairs.length; i++) {
        nv = pairs[i].split("=", 2);
        n = decodeURIComponent(nv[0]);
        v = decodeURIComponent(nv[1]);

        if (!parms.hasOwnProperty(n)) parms[n] = [];
        parms[n].push(nv.length === 2 ? v : null);
    }
    return parms;
}
var urlString = document.location.href;
var urlParams = parseURLParams(urlString);
if(urlParams){
	RI = urlParams.ri[0];
}

function loadQuestion (questionIndex) {
	var q = questions[questionIndex];
	questionEl.textContent = (questionIndex + 1) + '. ' + q.question;
	opt1.textContent = q.option1;
	opt2.textContent = q.option2;
	opt3.textContent = q.option3;
	opt4.textContent = q.option4;
};

function loadNextQuestion () {
	var selectedOption = document.querySelector('input[type=radio]:checked');
	if(!selectedOption){
		alert('Please select one answer!');
		return;
	}
	var answer = selectedOption.value;
	if(questions[currentQuestion].answer == answer & currentQuestion <= 2){
		score += 1;
	}
	if(questions[currentQuestion].answer == answer & currentQuestion >= 3 & currentQuestion <= 5 ){
		score += 2;
	}
	if(questions[currentQuestion].answer == answer & currentQuestion == 6 ){
		score += 3;
	}


	selectedOption.checked = false;
	currentQuestion++;
	if(currentQuestion == totQuestions - 1){
		nextButton.textContent = 'Finish/ Termine';
	}
	if(currentQuestion == totQuestions){
		container.style.display = 'none';
		resultCont.style.display = '';
		questionEll.textContent = 'Votre Score RG: ' + score;
		document.getElementById("save").href="Enregistrement.html?ri="+RI+"&rg="+score;
		return;
	}
	



	if(score <= 1 ){
		interpretationCont.textContent = 'Low risk / Risque faible, veuillez cliquer sur enregistrement.';
		
	}
	if(score >= 2 & score <= 4 ){
		interpretationCont.textContent = 'Moderate risk / Risque modere, veuillez cliquer sur enregistrement.';
		
	}
	if(score >= 5){
		interpretationCont.textContent = 'High risk / Risque eleve, veuillez cliquer sur enregistrement.';
	}
	

	
	loadQuestion(currentQuestion);
}

loadQuestion(currentQuestion);