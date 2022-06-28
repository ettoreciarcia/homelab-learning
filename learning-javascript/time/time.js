// nomeFile = "test"

// const today = new Date();
// const yyyy = today.getFullYear();
// let mm = today.getMonth() + 1; // Months start at 0!
// let dd = today.getDate();
// let h  = today.getHours();
// let m = today.getMinutes();
// let s = today.getSeconds();


// if (dd < 10) dd = '0' + dd;
// if (mm < 10) mm = '0' + mm;
// if (h < 10) h = '0' + h;
// if (m < 10) m = '0' + m;
// if (s < 10) s = '0' + s;
 
// formatTime = dd + '/' + mm + '/' + yyyy + '-' + h + ':' + m + ':' + s;

// const newString = formatTime.concat(nomeFile);


// stringa = 'files/ExportTag_esempio.csv'
// stringToRemove = '/files/'
// var result = stringa.replace('files/', '');
// console.log(result);

// const test = new luxon();
// console.log(luxon.DateTime.now().setZone(Europe/Paris))

// let yourDate = new Date()
// console.log(yourDate.toISOString().split('T')[0]);
// console.log(yourDate.toLocaleDateString());

var ts = Math.round((new Date()).getTime() / 1000);
console.log(ts);