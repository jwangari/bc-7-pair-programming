var rootRef = new Firebase('https://pairprogram.firebaseio.com/');
username = $('#username').text();
session_id = $('#session_id').text();
sessionsRef = 'https://pairprogram.firebaseio.com/'
function init() {
  //// Initialize Firebase.
  var firepadRef = getExampleRef();
  // TODO: Replace above line with:
  // var firepadRef = new Firebase('<YOUR FIREBASE URL>');
  //// Create ACE
  var editor = ace.edit("firepad");
  editor.setTheme("ace/theme/textmate");
  var session = editor.getSession();
  session.setUseWrapMode(true);
  session.setUseWorker(false);
  session.setMode("ace/mode/javascript");
  //// Create Firepad.
  var firepad = Firepad.fromACE(firepadRef, editor, {
    defaultText: ' '
  });
}
// Helper to get hash from end of URL or generate a random one.
function getExampleRef() {
  var ref = new Firebase('https://pairprogram.firebaseio.com/');
  var hash = window.location.hash.replace(/#/g, '');
  if (hash) {
    ref = ref.child(hash);
  } else {
    ref = ref.push(); // generate unique location.
    window.location = window.location + '#' + ref.key(); // add it as a hash to the URL.
  }
  // if (typeof console !== 'undefined')
  //   console.log('Firebase data: ', ref.toString());
  setTimeout(function() {
    saveUserSession();
    console.log('Saving session');
    }, 5000);
  return ref;
}
window.onload = init;

var saveUserSession = function() {
    sessionInfo = {
        username: $('#username').text(),
        session: window.location.hash.replace(/#/g, '')
    }

    var rootRef = new Firebase('https://pairprogram.firebaseio.com/');
    childRef = $('#username').text();
    var sessionsRef = rootRef.child(childRef);
    pushOnline(sessionInfo, sessionsRef);
}

var pushOnline = function(object, ref) {
    var newRef = ref.push();
    newRef.set(object);
}

        