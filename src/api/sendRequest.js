export const sendRequest = (requestType, requestURL, data) => {
  var xhr = new XMLHttpRequest();
  const baseURL = "http://localhost:8000/";
  return new Promise((resolve, reject) => {
    xhr.onreadystatechange = (e) => {
      if (xhr.readyState !== 4) {
        return;
      }

      if (xhr.status === 200) {
        resolve(JSON.parse(xhr.responseText));
      } else {
        console.log("request_error");
      }
    };
    xhr.open(requestType, baseURL + requestURL);
    xhr.send(data);
  });
};
