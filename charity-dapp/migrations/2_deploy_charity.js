const Charity = artifacts.require("Charity");

module.exports = function (deployer) {
  // Deploy the Charity contract
  deployer.deploy(Charity);
};
