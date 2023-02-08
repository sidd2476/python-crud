from flask import Flask, jsonify
import boto3

app = Flask(__name__)
s3 = boto3.client('s3')
@app.route('/list-bucket-content/', defaults={'path': ''})
@app.route('/list-bucket-content/<path>')
def list_bucket_content(path):
    # return ("hello " + path) 
    if path:
        # Get the contents of a specific path in the S3 bucket
        response = s3.list_objects(Bucket='terraform-test-sid', Prefix=path)
        print("1")
    else:
        # Get the top level contents of the S3 bucket
        response = s3.list_objects(Bucket='terraform-test-sid')
        print("2")

    # Return a JSON response with the contents of the S3 bucket
    return jsonify({'Contents': response})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
