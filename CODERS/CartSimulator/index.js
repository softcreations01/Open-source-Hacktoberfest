const prompt = require("prompt-sync")();

function cartSimulator() {
  const cart = {
    cartArray: [],
    addToCart(item) {
      this.cartArray.push(item);
      console.log(`${item} added to cart successfully! \n`);
    },
    removeFromCart(item) {
      const itemIndex = this.cartArray.findIndex((value) => value === item);

      if (itemIndex === -1) {
        console.log(`${item} not found in cart \n`);
      } else {
        this.cartArray.splice(itemIndex, 1);
        console.log(`${item} removed from cart successfully! \n`);
      }
    },
    standBy() {
      let stopSimulator = false;

      while (!stopSimulator) {
        console.log(
          "Input 'add' to add an item \nInput 'remove' to remove an item \nInput 'show-items' to show the items in cart \nInput 'length' to show the number of items in the cart \nInput 'exit' to exit the program \n"
        );
        let command = prompt("Command: ");

        switch (command.trim()) {
          case "add":
            console.log("Type the product you would like to add");
            const itemToAdd = prompt("Product: ");
            cart.addToCart(itemToAdd);
            break;

          case "remove":
            console.log("Type the product you would like to remove");
            const itemToRemove = prompt("Product: ");
            cart.removeFromCart(itemToRemove);
            break;

          case "show-items":
            console.log(`${cart.cartArray.join(", ")} \n`);
            break;

          case "length":
            console.log(`${cart.cartArray.length} \n`);
            break;

          case "exit":
            console.log("Bye \n");
            stopSimulator = true;
            break;

          default:
            console.log("Error: Unidentified Command! \n");
            break;
        }
      }
    },
  };

  return cart.standBy;
}
const startSimulation = cartSimulator();
startSimulation();
