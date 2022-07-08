// const name = '49552/temp/miofile.csv'

// value = name.split('/')
// console.log(value[0])


// const name = "batch-update-poste-test/6675/nomefile.csv"

// value = name.split('/')
// console.log(value)

// MyString = value[1].concat(value[2])

// console.log(MyString)


// const name1 = name.replace('batch-update-poste-test/','')
// console.log(name1)

// a = 'Ciao'
// b = 'Mi'
// c = 'Surprise'

// MyNewStr = a.concat(b.concat(c))

// console.log(MyNewStr)


const Bucket = 'batch-update-poste-test'
const bucketName = bucket.concat('/');
console.log("bucketName : " + bucketName);

const fileName = event.Records[0].s3.object.key.replace(bucketName, '');
console.log('fileName: ' + fileName);

const subscriptionID = fileName.split('/')[0].concat('/');
console.log('subscriptionID : ' + subscriptionID);

const onlyFileName = fileName.split('/')[1].concat('/');
console.log('onlyFileName : ' + onlyFileName);

//const fileName = event.Records[0].s3.object.key.replace('6675/files/', '');

const newNameFile = subscriptionID.concat(formatTime.concat(onlyFileName))
console.log('newNameFile : ' newNameFile);