export const sendRequest = (requestType, requestURL, data) => {
    var xhr = new XMLHttpRequest();

    return new Promise((resolve, reject) => {
        xhr.onreadystatechange = (e) => {
            if (xhr.readyState !== 4) {
                return;
            }

            if (xhr.status === 200) {
                resolve(JSON.parse(xhr.responseText));
            } else {
                console.log('request_error');
            }
        };
        xhr.open(requestType, requestURL);
        xhr.send(data);
    });
}
