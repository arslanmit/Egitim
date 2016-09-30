// POST /codecademy/learn-http HTTP/1.1
// Host: www.codecademy.com
// Content-Type: text/html;
// <?xml version="1.0" encoding="utf-8"?>
//<strin

/*
skyscanner
http://portal.business.skyscanner.net/en-gb/accounts/login/
*/

/*
app.all('*', function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS');
    res.header('Access-Control-Allow-Headers', 'accept, content-type, x-parse-application-id, x-parse-rest-api-key, x-parse-session-token');
    // intercept OPTIONS method
    if ('OPTIONS' == req.method) {
        res.send(200);
    }
    else {
        next();
    }
});
*/

var SkyscannerPost;
SkyscannerPost = "http://partners.api.skyscanner.net/apiservices/pricing/v1.0";
var SkyscannerGet;
SkyscannerGet="http://partners.api.skyscanner.net/apiservices/browsedates/v1.0/GB/GBP/en-GB/LON/JFK/anytime/anytime?apiKey=am296617236898565695386145032921";


var CodeCademyXml;
var CodeCademyXmlLocal;

//CodeCademyXml="https://www.codecademy.com/files/samples/javascript_learn_apis.xml";
CodeCademyXml="http://partners.api.skyscanner.net/apiservices/browsedates/v1.0/GB/GBP/en-GB/LON/JFK/anytime/anytime?apiKey=prtl6749387986743898559646983194";

CodeCademyXmlLocal="javascript_learn_apis.xml";

var xhr = new XMLHttpRequest();
//var xhrLocal = new XMLHttpRequest();

xhr.open("GET", CodeCademyXml, false);
//xhrLocal.open("GET", CodeCademyXmlLocal, false);

//xhr.send();
//xhrLocal.send();

console.log(xhr.status);
console.log(xhr.statusText);

//console.log(xhrLocal.status);
//console.log(xhrLocal.statusText);

xmlDocument = xhr.responseXML;
console.log(xmlDocument);

//console.log(xmlDocument.childNodes['0'].textContent);


//xmlLocalDocument = xhrLocal.responseXML;
//console.log(xmlLocalDocument.childNodes['0'].textContent);

var apiKey = "am296617236898565695386145032921";


//var demo = '{"pets": { "name": "Jeffrey", "species": "Giraffe"}}';
//console.log(demo);
//var json = JSON.parse(demo);
//console.log(json);

/*
http://partners.api.skyscanner.net/apiservices/pricing/v1.0/GB/GBP/en-GB/LON/JFK/2017-01-01/2017-01-05?apiKey=am296617236898565695386145032921
*/

