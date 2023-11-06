let value = (data) =>{
    return new Promise((resolve, reject)=>{
        if (isNaN(data)) {
            reject('error');
        }
        else if (data % 2 === 0) {
            setTimeout(() => {
                reject('even');
            }, 2000);
        }
        else {
            setTimeout(() => {
                resolve('odd');
            }, 1000);
        }
    });
};

value('e').then((fromResolve)=>{
    console.log(fromResolve);
}).catch((fromReject) => {
    console.log(fromReject);
});

value(0).then((fromResolve)=>{
    console.log(fromResolve);
}).catch((fromReject) => {
    console.log(fromReject);
});

value(1).then((fromResolve)=>{
    console.log(fromResolve);
}).catch((fromReject) => {
    console.log(fromReject);
});