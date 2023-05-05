
function menor(){
    var y;
    var idade = prompt("Digite sua idade: ");

 

    if (idade == 15 || idade == 16 || idade == 17){
        y = "O sr.(a) tem menos de 18 anos, sua idade é:" + idade + "anos.";
        document.getElementById("anos").innerHTML=y;
        window.location="/responsavel/responsavel";
      
    }
    else if (idade >= 18){
        y = "O sr.(a) tem mais de 18 anos. Sua idade é " + idade + "anos";
        document.getElementById("anos").innerHTML=y;
        window.location="/accounts/profile";
    }
    else if (idade < 15){
        y = "O sr. não pode se cadastrar. Não tem a idade minima: 16 anos.";
        document.getElementById("anos").innerHTML=y;
        
    }
    
    else{
        y = "Sua idade encontra-se incorr!";
        document.getElementById("anos").innerHTML=y;
     
    }
}
