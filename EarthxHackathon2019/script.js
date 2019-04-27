// const Http = new XMLHttpRequest();
// const url='localhost:5000/user/111';
// Http.open("GET", url);
// Http.send();
// Http.onreadystatechange=(e)=>{
// console.log(Http.responseText)
// }

let userSignup = function (password, email, numberOfPeople, gallonsUsed, threshold) {
  return new Promise(function (fulfill, reject) {
  const xhttp = new XMLHttpRequest();
  const json = {
    "password": password,
    "email": email,
    "numberOfPeople": numberOfPeople,
    "gallonsUsed": gallonsUsed,
    "threshold": threshold
  };
  xhttp.open("POST", "/user/" + email, true);
  xhttp.send(json);
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
});
