// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat")


//return the ether balance of the given addresss
async function getBalance(address) {
  const balanceBigInt = await hre.ethers.provider.getBalance(address);
  return hre.ethers.utils.formatEther(balanceBigInt)
}

//Logs the Ether balances for a list of addresses.
async function printBalances(addresses){
  let idx=0;
  for (const address of addresses){
    console.log(`Address of ${idx} balance: `, await getBalance(address));
    idx++;
  }
}

//Logs the memos stored on-chain from coffee purchases.
async function printMemos(memos){
  for (const memo of memos){
    const timestamp=memo.timestamp;
    const tipperAddress=memo.from;
    const tipper=memo.name;
    const message=memo.message;
    console.log(`At ${timestamp},${tipper} of address ${tipperAddress} said: "${message}"`);
  }
}

async function main() {
  //Get example accounts 
  const [owner, tipper, tipper2, tipper3] = await hre.ethers.getSigners()
  //Get the contract to deploy & deplo it
  const BuyMeACoffee = await hre.ethers.getContractFactory("BuyMeACoffee");
  const buyMeACoffee = await BuyMeACoffee.deploy();
  const { target }=buyMeACoffee
  console.log("Contract is deployed to ",target)
  //Check balance before buying coffee
  const addresses = [owner.address, tipper.address, target]
  console.log("===========start============")
  await printBalances(addresses)

  //Withdraw funds

  //Check balaces after the withdrawal

  //Read all the memos left for the owner
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
