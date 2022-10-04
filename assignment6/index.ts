import * as functions from "firebase-functions";
import * as admin from "firebase-admin";
admin.initializeApp();

exports.combinName = functions.firestore.document("/books/{isbn}")
    .onCreate( (snap, context) => {
      const firName = snap.data().author_first;
      const lasName = snap.data().author_lastname;
      const ID = context.params.isbn;
      const whNa = firName + " " + lasName;
      return admin.firestore().collection("books")
          .doc(ID).set({wholeName: whNa}, {merge: true});
    });