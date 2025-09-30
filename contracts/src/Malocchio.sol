// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {ERC721Enumerable} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";

contract Malocchio is ERC721, ERC721Enumerable, Ownable {
    constructor() ERC721("Malocchios", "Mallocchios") Ownable(msg.sender) {}


    uint price = 9 ether / 1000; //0.009 ETH
    uint maxSupply = 3333;
    uint256 public _nextTokenId = 1;

    function uintToFourDigitString(uint256 num) public pure returns (string memory) {
        bytes memory str = new bytes(4);

        // Extract digits from right to left
        for (uint256 i = 0; i < 4; i++) {
            str[3 - i] = bytes1(uint8(48 + (num % 10))); // ASCII '0' = 48
            num /= 10;
        }

        return string(str);
    }

    function mint(uint numberOfMints) public payable {
        require(msg.value >= price * numberOfMints, "Insufficient funds. You must pay the price.");
        require(_nextTokenId + numberOfMints <= maxSupply, "Max supply reached.");
        uint256 tokenId = _nextTokenId;
        for (uint256 i = 0; i < numberOfMints; i++) {
            _safeMint(msg.sender, tokenId + i);
        }
        _nextTokenId += numberOfMints;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(tokenId < _nextTokenId, "ERC721Metadata: URI query for nonexistent token");
        string memory baseURI = _baseURI();
        return string(abi.encodePacked(baseURI, "malocchio", uintToFourDigitString(tokenId), ".json"));
    }

    function _baseURI() internal view override returns (string memory) {
        return "ipfs://bafybeigbochupyjj5imitg3gdmt3qqoedlygkuy76tms6vfjc764owtine/";
    }

    function adminCashout() public onlyOwner {
        bal = address(this).balance;
        //50% split between the 2 artists
        payable(0x7C46E09DDF369dfc338D09675175D00b68fC61a3).transfer(bal / 2);
        payable(0xf3a8f86A476fd83dF2cD1471BcB6d97F7AFEb38B).transfer(bal / 2);
    }

    function setPrice(uint newPrice) public onlyOwner {
        price = newPrice;
    }

    // Required overrides for multiple inheritance
    function _increaseBalance(address account, uint128 value) internal override(ERC721, ERC721Enumerable) {
        super._increaseBalance(account, value);
    }

    function _update(address to, uint256 tokenId, address auth) internal override(ERC721, ERC721Enumerable) returns (address) {
        return super._update(to, tokenId, auth);
    }

    function supportsInterface(bytes4 interfaceId) public view override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}