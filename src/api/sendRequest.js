export const sendRequest = (requestType, requestURL, data) => {
    const xhr = new XMLHttpRequest();

    xhr.open(requestType,requestURL);
    xhr.setRequestHeader("Content-Type", "application/json");
    
    xhr.responseType = "json";
    xhr.addEventListener("readystatechange", ()=>{
        if(xhr.readyState === xhr.DONE){
            return(xhr.response);
        }
    })
    
    xhr.send(data);


}