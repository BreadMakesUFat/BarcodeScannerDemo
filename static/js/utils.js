// The content for one post request goes here 
// ScanContent holds all entities for one destination
class ScanContent {

    destination;
    bons = [];
    recipients = [];
    amounts = [];

    constructor(destination) {
        this.destination = destination;
    }

    addBon(bon) {
        this.bons.push(bon);
    }

    addRecipient(recipient) {
        this.recipients.push(recipient);
    }

    addAmount(amount) {
        this.amounts.push(amount);
    }

    json() {
        return JSON.stringify(this);
    }

    sendPost() {

        // content of the post request
        const content = {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: this.json()
        };

        // send post request to server and display result as popup
        const response = fetch("/bookings/", content) 
            .then(resp => {
                if (resp.ok) {
                    alert("The booking was successfull.");
                }
                else {
                    alert("There was an error!");
                }
            }
        );

    }

}

// Scenes that hold forms 
// Each scene points to the following one 

class Scene {
    // id of the corresponding div
    id;

    constructor(id) {
        this.id = id;
    }

    disable() {
        document.getElementById(this.id).style.display = "none";
    }

    enable() {
        document.getElementById(this.id).style.display = "table-cell";
    }

    nextScene(scene) {
        this.disable();
        scene.enable();
    }
}


// Helper functions

function focus(id) {
    // TODO: implement
}

function clearText(id) {
    document.getElementById(id).value = "";
}
