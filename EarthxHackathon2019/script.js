// const Http = new XMLHttpRequest();
// const url='localhost:5000/user/111';
// Http.open("GET", url);
// Http.send();
// Http.onreadystatechange=(e)=>{
// console.log(Http.responseText)
// }

let userSignup = function (password, email, numberOfPeople, username) {
  return new Promise(function (fulfill, reject) {
  const xhttp = new XMLHttpRequest();
  const json = {
    "password": password,
    "email": email,
    "username": username,
    "numberOfPeople": parseInt(numberOfPeople),
    "gallons": 0,
    "threshold": 10
  };
  url = "http://localhost:5000/user/" + username;
//   '?password=' + password + '&numberOfPeople=' + numberOfPeople
  xhttp.open("POST", url, true);
  xhttp.setRequestHeader('Content-Type', 'application/json');
  xhttp.send(JSON.stringify(json));
  xhttp.onload = function (request, event) {
            console.log(request, event);
            console.log(xhttp.responseText);
            let response = xhttp.responseText;
            fulfill(response);
        };

        xhttp.onerror = function (request, event) {
            console.log(request, event);
            reject ("request not processed succesfully");
        };
});}

let userLogin = function(username, password) {

    return new Promise(function (fulfill, reject) {
        const xhttp = new XMLHttpRequest();
        url = "http://localhost:5000/user/" + password + username;
        xhttp.open("GET", url, true);
        xhttp.setRequestHeader('Content-Type', 'application/json');
        xhttp.send();
        xhttp.onload = function (request, event) {
                  console.log(request, event);
                  console.log(xhttp.responseText);
                  let response = xhttp.responseText;
                  sessionStorage.setItem("UserInfo", response);
                  fulfill(response);
              };

              xhttp.onerror = function (request, event) {
                  console.log(request, event);
                  reject ("request not processed succesfully");
              };
      });

}

let LoadMain = function() {
   info = JSON.parse(sessionStorage.getItem("UserInfo"))
   document.getElementById("usage").innerHTML = "You have used " + info["gallons"] + " out of " + info['threshold'] + "gallons";
}
//
// document.getElementById("login").onclick = function () {
//     const UserInfo =
// };
