<!DOCTYPE html>
<html>
<head>
    <script src="https://sdk.amazonaws.com/js/aws-sdk-2.1303.0.min.js"></script>
</head>
<body>
    <input type="file" id="file" /><button onclick="upload()">Upload</button>
    <script>
        AWS.config.update({region: 'us-east-1', credentials: new AWS.CognitoIdentityCredentials({IdentityPoolId: 'YOUR_IDENTITY_POOL_ID'})});
        const s3 = new AWS.S3({params: {Bucket: 'YOUR_BUCKET_NAME'}});
        function upload() { const f = document.getElementById('file').files[0]; s3.upload({Key: f.name, Body: f}, (e, d) => alert(e ? 'Error: ' + e : 'Uploaded: ' + d.Location)); }
    </script>
</body>
</html>

