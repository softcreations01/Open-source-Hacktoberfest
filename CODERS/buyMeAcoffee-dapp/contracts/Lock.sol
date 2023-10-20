// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.19;

contract BuyMeACoffee{
    //Event to emit when memo is created
    event NewMemo(
        address indexed from,
        uint256 timestamp,
        string name,
        string message
    );

    //Memo struct.
    struct Memo{
        address from;
        uint timestamp;
        string name;
        string message;
    }

    //List of all the meos received from friends
    Memo[] memos;

    //Address of the contract deployer
    address payable owner;

    //Deoloy Logic
    constructor(){
        owner=payable(msg.sender);
    }

    /**
     * @dev buy a coffee for contract ower
     * @param _name name of the coffee buyer
     * @param _message a nice message for the coffee buyer
     */

    function buyCoffee(string memory _name, string memory _message) public payable{
        require(msg.value>0,"Can't buy a coffee with 0 eth");

        //Add the memo to the array of Memos(i.e.,Storage)
        memos.push(Memo(
            msg.sender,
            block.timestamp,
            _name,
            _message
        ));

        //Emit a log event when a new Memo is created
        emit NewMemo(
            msg.sender,
            block.timestamp,
            _name,
            _message
        );
    }

    /**
     * @dev send the entire balance stored in this contract t the owner
     */

    function withDrawTips() public {
        require(owner.send(address(this).balance)); 
        //here in this above line
        /**
         * address(this) represents the addresss of the smart contract
         * .balance retreives all the balance of the smart contract
         * owner.send recieves all the balnce from the smart contract to the address of the owner assigned
         * require function ensures that all the money or ether is being transffered form the smart contract to the owner whenever the function is callled.
         */
    }

    /**
     * @dev retrieve all the memos recieved and stored on the blockchain
     */
    function getMemos() public view returns(Memo[] memory){
        return memos;
    }


}
