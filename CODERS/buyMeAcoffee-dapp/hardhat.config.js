require("@nomicfoundation/hardhat-toolbox");
require("@nomicfoundation/hardhat-ethers");
require("dotenv").config();


const GOERLI_URL=process.env.GOERLI_URL;
const PRIVATE_KEY=process.env.PRIVATE_KEY;

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.19",
  networks:{
    goerli:{
      url:GOERLI_URL,
      accounts:[PRIVATE_KEY]
    }
  }
};
