var currentQuestion = 0;
var score = 0;
var totQuestions = questions.length;

var container = document.getElementById('quizContainer');
var questionEl = document.getElementById('question');
var opt1 = document.getElementById('opt1');
var opt2 = document.getElementById('opt2');
var opt3 = document.getElementById('opt3');
var opt4 = document.getElementById('opt4');
var nextButton = document.getElementById('nextButton');
var resultCont = document.getElementById('result');



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
	console.log("params : ", urlParams)
	document.getElementById("scoreRI").value=urlParams.ri[0]
	if(urlParams.rg){
		document.getElementById("scoreRG").value=urlParams.rg[0];
	}else {
		document.getElementById("scoreRG").value="N/A";
	}
}

function loadQuestion (questionIndex) {
	var q = questions[questionIndex];
	questionEl.textContent = (questionIndex + 1) + '. ' + q.question;
	opt1.textContent = q.option1;
	opt2.textContent = q.option2;
	// opt3.textContent = q.option3;
	// opt4.textContent = q.option4;
};

function loadNextQuestion () {
	var selectedOption = document.querySelector('input[type=radio]:checked');
	if(!selectedOption){
		alert('Please select one answer!');
		return;
	}
	var answer = selectedOption.value;
	if(questions[currentQuestion].answer == answer & currentQuestion <= 7){
		score += 1;
	}
	if(questions[currentQuestion].answer == answer & currentQuestion >= 8 & currentQuestion <= 9 ){
		score += 2;
	}
	if(questions[currentQuestion].answer == answer & currentQuestion >= 10 & currentQuestion <= 15){
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
		questionEll.textContent = 'Votre Score RI: ' + score;
		document.getElementById("save").href="Enregistrement.html?ri="+score;
		if(score >= 6){
			console.log("score : ", score)
			document.getElementById("btnScd").style.display="inline-block";
			document.getElementById("secondTest").href="Evaluation-gravite.html?ri="+score;
		}
		return;
	}
	



	if(score <= 2 ){
		interpretationCont.textContent = 'May be stress related and observe / Observer, veuillez cliquer sur enregistrement.';
		
	}
	if(score >= 3 & score <= 5 ){
		interpretationCont.textContent = 'Hydrate properly and proper personal hygiene. Observe and re-evaluate after 2 days / Hydrater avec hygiene adequate reevaluer apres 2 jours, veuillez cliquer sur enregistrement.';
		
	}
	if(score >= 6 & score <= 9 ){
		interpretationCont.textContent = 'Seek a consultation with Doctor / Consultation Medicale, veuillez suivre le second test RG et ensuite appelez immediatement un numÃ©ro vert de votre localitÃ©. ';
		
		
	}
	if(score >= 10 & score <= 21 ){
		interpretationCont.textContent = 'Need for emergency care / a besoin des soins en urgence, veuillez suivre le second test RG et ensuite appelez immediatement un numÃ©ro vert de votre localitÃ©.';
		
	}

	loadQuestion(currentQuestion);
}

  
loadQuestion(currentQuestion);