function validate(){
    var nameri = document.getElementById("Votre Score RI").value;
    var namerg = document.getElementById("Votre Score RG").value;
     var name = document.getElementById("Noms et Prenoms").value;
     
    var age = document.getElementById("Ã‚ge").value;
    var quartier = document.getElementById("Quartier").value;
    var ville = document.getElementById("Ville").value;
    var phone = document.getElementById("Contact Personnel").value;
    var percontact = document.getElementById("Personne Ã  contacter").value;
    var sexe = document.getElementById("Sexe").value;
    var adpro = document.getElementById("Addresse professionnelle").value;
    var email = document.getElementById("Email").value;
    var error_message = document.getElementById("error_message");
    
    error_message.style.padding = "10px";
    
  sex = name="entry.1512074174"
  
    var text;
  
    if(nameri.length > 2){
      text = "Entrez un correct Score RI";
      error_message.innerHTML = text;
      return false; 
    }  
    if(namerg.length > 2){
      text = "Entrez un correct Score RG";
      error_message.innerHTML = text;
      return false; 
    }  
  
    if(name.length < 5){
      text = "Entrez plus de lettres";
      error_message.innerHTML = text;
      return false;  
    }
    var sexe = document.querySelector('input[type=radio]:checked');
      if(!sexe){
      text = "selectionnez votre sexe";
      error_message.innerHTML = text;
      return false;
      }
    if(age.length > 2){
      text = "Entrez un Ã¢ge correct";
      error_message.innerHTML = text;
      return false;
    }
    if(quartier.length < 5){
      text = "Entrez une ville correct";
      error_message.innerHTML = text;
      return false;}
    
    if(ville.length < 5){
      text = "Entrez une ville correct";
      error_message.innerHTML = text;
      return false;}
  
    if(isNaN(phone) || phone.length != 9){
      text = "Entrez un correct numÃ©ro personnel";
      error_message.innerHTML = text;
      return false;
    }
    if(isNaN(percontact) || percontact.length != 9){
      text = "Entrez un numÃ©ro Valide";
      error_message.innerHTML = text;
      return false;}
  
      if(adpro.length < 10){
        text = "Entrez une addresse correct";
        error_message.innerHTML = text;
        return false;}
    
  
    if(email.indexOf("@") == -1 || email.length < 6){
      text = "Entrez un email valide";
      error_message.innerHTML = text;
      return false;
  
    }
    document.getElementById("iVotre Score RI").value = score
    alert("Form Submitted Successfully!");
    return true;
  }