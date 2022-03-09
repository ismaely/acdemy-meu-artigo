function convertHtmlPdf() {
    const element = document.getElementById('reciboInscricao');

    var name = moment().format("DD-MM-YYYY-h:m:s");
    namefile = name + ".pdf";
    html2pdf().from(element).save(namefile);
}


function take_snapshot() {
    // take snapshot and get image data
    Webcam.snap(function (data_uri) {
        // display results in page
        document.getElementById("results").innerHTML = '<img id="imageprev" src="' + data_uri + '"/>';
        document.getElementById("result").innerHTML = '<img id="imageprev"  class="rounded-circle" src="' + data_uri + '"/>';
        document.getElementById('fotoSalva').value = data_uri;
    });

    Webcam.reset();
}


function saveSnap() {
    // Get base64 value from <img id='imageprev'> source
    //console.log(data_uri)

    //var base64image = document.getElementById("imageprev").src;

    /**
     * Webcam.upload(base64image, "upload.php", function (code, text) {
        console.log("Save successfully");
        //console.log(text);
    });
    **/
}