const operators = [
  'Operator 1',
  'Operator 2',
  'Operator 3'
];

const accounts = [
  'Account 1',
  'Account 2',
  'Account 3'
];

const cards = [
  'Card 1',
  'Card 2',
  'Card 3'
];

function populateList(elementId, data) {
  const listElement = document.getElementById(elementId);
  listElement.innerHTML = '';

  data.forEach(item => {
    const listItem = document.createElement('li');
    listItem.textContent = item;
    listElement.appendChild(listItem);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  populateList('operator-list', operators);
  populateList('account-list', accounts);
  populateList('card-list', cards);
});
