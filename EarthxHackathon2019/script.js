const Http = new XMLHttpRequest();
const url='localhost:5000/user/111';
Http.open("GET", url);
Http.send();
Http.onreadystatechange=(e)=>{
console.log(Http.responseText)
}