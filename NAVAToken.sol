

 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NAVAToken is ERC20 {
    constructor(uint256 initialSupply)
        ERC20("NAVA Token", "NAVA")
    {
        require(initialSupply > 0, "Supply must be positive");
        _mint(msg.sender, initialSupply * 10 ** decimals());
    }
}
