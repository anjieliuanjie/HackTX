document.getElementById('DanceOn').addEventListener('click', async() =>{
  tabId = await getTabId() //get the id of the current tab i'm in
  //alert('button clicked!') // like print(), create a pop up of it's own
  //send message to content script
  chrome.tabs.sendMessage(tabId, "dance_on", (response) => {
    //alert('message sent to content script!')
  })

})
//listen to click even, once there's a click, this event is called








/*
// listening for a click event on the #DanceOn <button>
document.getElementById("DanceOn").addEventListener('click', async () => {

  // get the ID of the current tab
  tabId = await getTabId()

  // send a message to the content script running in the tab with tabId
  chrome.tabs.sendMessage(tabId, "dance_on", (response) => {
    // for testing purposes
    // alert('successfully sent message to content script');
    
    // EXTRA CODE NOT COVERED IN WORKSHOP
    // get a response from the content script
    if (response === 'success') {
      // do something after you find receive a response/reply
      // from content.js that the message has been received successfully 
    }
  });

});

// function to get the tabId of the current tab
async function getTabId() {
  let queryOptions = { active: true, currentWindow: true };
  let tabs = await chrome.tabs.query(queryOptions);
  return tabs[0].id;
}
*/