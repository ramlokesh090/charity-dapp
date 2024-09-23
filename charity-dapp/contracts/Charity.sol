// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

contract Charity {
    address public owner;
    mapping(address => uint) public donations;

    event DonationReceived(address indexed donor, uint amount);

    constructor() {
        owner = msg.sender;
    }

    function donate() public payable {
        require(msg.value > 0, "Donation must be greater than 0");
        donations[msg.sender] += msg.value;
        emit DonationReceived(msg.sender, msg.value);
    }

    function getBalance() public view returns (uint) {
        return address(this).balance;
    }

    function withdraw(uint amount) public {
        require(msg.sender == owner, "Only owner can withdraw funds");
        require(amount <= address(this).balance, "Not enough funds");
        payable(owner).transfer(amount);
    }
}
