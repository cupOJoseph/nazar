// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts ^5.0.0
pragma solidity ^0.8.27;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {ERC721Enumerable} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

/// @custom:security-contact @Cupojoseph
contract Eyes is ERC721, ERC721Enumerable, Ownable {
    uint256 private _nextTokenId;

    uint ownerMints = 0;

    uint256 public maxSupply;

    uint public price;

    constructor(address initialOwner, uint256 _maxSupply, uint _price)
        ERC721("Eyes", "EYES")
        Ownable(initialOwner)
        maxSupply = _maxSupply
        price = _price
    {}

    function ownerMint(address to) public onlyOwner returns (uint256) {
        require(ownerMints < 100, "Owner can only mint 100");
        require(tokenId < maxSupply, "Max supply reached.");
        uint256 tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        return tokenId;
    }

    function mint(address to) public payable returns (uint256) {
        require(msg.value >= price, "Insufficient funds. You must pay the price.");
        require(tokenId < maxSupply, "Max supply reached.");
        uint256 tokenId = _nextTokenId++;
        _safeMint(to, tokenId);
        return tokenId;
    }

    function batchMint(uint256 amount) public payable returns (uint256) {
        require(msg.value >= price * amount, "Insufficient funds. You must pay the price.");
        require(tokenId < maxSupply, "Max supply reached.");

        uint256 startTokenId = _nextTokenId;
        for (uint256 i = 0; i < amount; ) {
            uint256 tokenId = _nextTokenId++;
            _safeMint(msg.sender, tokenId);

            unchecked {
                ++i;
        }
    }

    // The following functions are overrides required by Solidity.

    function _update(address to, uint256 tokenId, address auth)
        internal
        override(ERC721, ERC721Enumerable)
        returns (address)
    {
        return super._update(to, tokenId, auth);
    }

    function _increaseBalance(address account, uint128 value)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._increaseBalance(account, value);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
