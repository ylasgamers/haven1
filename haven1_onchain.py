from web3 import Web3, HTTPProvider
from eth_abi import encode
from datetime import datetime, timedelta
import json
import time
import random
import secrets
import string

print(f'Daily Task Haven1 Onchain | @ylasgamers')
web3 = Web3(Web3.HTTPProvider('https://ethereum-sepolia-rpc.publicnode.com'))
chainId = web3.eth.chain_id
web3_hv = Web3(Web3.HTTPProvider('https://810.rpc.thirdweb.com'))
chainId_hv = web3_hv.eth.chain_id

#connecting web3
if  web3.is_connected() == True:
    print("Web3 Connected Sepolia...\n")
else:
    print("Error Connecting Please Try Again Exit...")
    exit()
if  web3_hv.is_connected() == True:
    print("Web3 Connected Haven1...\n")
else:
    print("Error Connecting Please Try Again Exit...")
    exit()
    
router_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH","type":"address"},{"internalType":"address","name":"_feeAddress","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"WETH","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"amountADesired","type":"uint256"},{"internalType":"uint256","name":"amountBDesired","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountTokenDesired","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"addLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"},{"internalType":"uint256","name":"liquidity","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountIn","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"reserveIn","type":"uint256"},{"internalType":"uint256","name":"reserveOut","type":"uint256"}],"name":"getAmountOut","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsIn","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"}],"name":"getAmountsOut","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"reserveA","type":"uint256"},{"internalType":"uint256","name":"reserveB","type":"uint256"}],"name":"quote","outputs":[{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidity","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETH","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"removeLiquidityETHSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermit","outputs":[{"internalType":"uint256","name":"amountToken","type":"uint256"},{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountTokenMin","type":"uint256"},{"internalType":"uint256","name":"amountETHMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityETHWithPermitSupportingFeeOnTransferTokens","outputs":[{"internalType":"uint256","name":"amountETH","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"},{"internalType":"uint256","name":"liquidity","type":"uint256"},{"internalType":"uint256","name":"amountAMin","type":"uint256"},{"internalType":"uint256","name":"amountBMin","type":"uint256"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"bool","name":"approveMax","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"removeLiquidityWithPermit","outputs":[{"internalType":"uint256","name":"amountA","type":"uint256"},{"internalType":"uint256","name":"amountB","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapETHForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForETHSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactTokensForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactETH","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMax","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapTokensForExactTokens","outputs":[{"internalType":"uint256[]","name":"amounts","type":"uint256[]"}],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
lpnft_abi = json.loads('[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH9","type":"address"},{"internalType":"address","name":"_tokenDescriptor_","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"Collect","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"DecreaseLiquidity","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"},{"indexed":false,"internalType":"uint128","name":"liquidity","type":"uint128"},{"indexed":false,"internalType":"uint256","name":"amount0","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"amount1","type":"uint256"}],"name":"IncreaseLiquidity","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WETH9","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"baseURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint128","name":"amount0Max","type":"uint128"},{"internalType":"uint128","name":"amount1Max","type":"uint128"}],"internalType":"struct INonfungiblePositionManager.CollectParams","name":"params","type":"tuple"}],"name":"collect","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"uint160","name":"sqrtPriceX96","type":"uint160"}],"name":"createAndInitializePoolIfNecessary","outputs":[{"internalType":"address","name":"pool","type":"address"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"internalType":"struct INonfungiblePositionManager.DecreaseLiquidityParams","name":"params","type":"tuple"}],"name":"decreaseLiquidity","outputs":[{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"amount0Desired","type":"uint256"},{"internalType":"uint256","name":"amount1Desired","type":"uint256"},{"internalType":"uint256","name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"internalType":"struct INonfungiblePositionManager.IncreaseLiquidityParams","name":"params","type":"tuple"}],"name":"increaseLiquidity","outputs":[{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint256","name":"amount0Desired","type":"uint256"},{"internalType":"uint256","name":"amount1Desired","type":"uint256"},{"internalType":"uint256","name":"amount0Min","type":"uint256"},{"internalType":"uint256","name":"amount1Min","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"internalType":"struct INonfungiblePositionManager.MintParams","name":"params","type":"tuple"}],"name":"mint","outputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"amount0","type":"uint256"},{"internalType":"uint256","name":"amount1","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"positions","outputs":[{"internalType":"uint96","name":"nonce","type":"uint96"},{"internalType":"address","name":"operator","type":"address"},{"internalType":"address","name":"token0","type":"address"},{"internalType":"address","name":"token1","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"int24","name":"tickLower","type":"int24"},{"internalType":"int24","name":"tickUpper","type":"int24"},{"internalType":"uint128","name":"liquidity","type":"uint128"},{"internalType":"uint256","name":"feeGrowthInside0LastX128","type":"uint256"},{"internalType":"uint256","name":"feeGrowthInside1LastX128","type":"uint256"},{"internalType":"uint128","name":"tokensOwed0","type":"uint128"},{"internalType":"uint128","name":"tokensOwed1","type":"uint128"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"refundETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowed","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowedIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"sweepToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"uint256","name":"index","type":"uint256"}],"name":"tokenOfOwnerByIndex","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount0Owed","type":"uint256"},{"internalType":"uint256","name":"amount1Owed","type":"uint256"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"uniswapV3MintCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"unwrapWETH9","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]')
token_abi = json.loads('[{"inputs":[{"internalType":"string","name":"_name","type":"string"},{"internalType":"string","name":"_symbol","type":"string"},{"internalType":"uint256","name":"initialSupply","type":"uint256"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
daily_abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"DailyStreak__CanNotRepairStreak","type":"error"},{"inputs":[{"internalType":"uint256","name":"currentTimestamp","type":"uint256"},{"internalType":"uint256","name":"canContinueAtTimestamp","type":"uint256"}],"name":"DailyStreak__TooEarlyTooContinueStreak","type":"error"},{"inputs":[],"name":"H1NativeBase__AlreadyInitialized","type":"error"},{"inputs":[{"internalType":"uint256","name":"fundsInContract","type":"uint256"},{"internalType":"uint256","name":"currentFee","type":"uint256"}],"name":"H1NativeBase__InsufficientFunds","type":"error"},{"inputs":[],"name":"H1NativeBase__InvalidFeeContract","type":"error"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"previousAdmin","type":"address"},{"indexed":false,"internalType":"address","name":"newAdmin","type":"address"}],"name":"AdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"beacon","type":"address"}],"name":"BeaconUpgraded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"feeContractAddressNew","type":"address"},{"indexed":false,"internalType":"address","name":"feeContractAddressPrev","type":"address"}],"name":"FeeAddressUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint8","name":"version","type":"uint8"}],"name":"Initialized","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"oldAddress","type":"address"},{"indexed":true,"internalType":"address","name":"newAddress","type":"address"}],"name":"ParticipationTokenUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":true,"internalType":"uint256","name":"streakContinueTimestamp","type":"uint256"},{"indexed":false,"internalType":"uint24","name":"daysInStreak","type":"uint24"},{"indexed":false,"internalType":"uint24","name":"streakTotal","type":"uint24"}],"name":"StreakContinued","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"}],"name":"StreakRepaired","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"implementation","type":"address"}],"name":"Upgraded","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TIME_TO_REPAIR","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"canContinueStreak","outputs":[{"internalType":"bool","name":"canContinue","type":"bool"},{"internalType":"uint256","name":"continueStreakTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"canRepairStreak","outputs":[{"internalType":"bool","name":"canRepair","type":"bool"},{"internalType":"uint256","name":"lastStreakContinuedTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"continueStreak","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getStreak","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getStreakHistory","outputs":[{"internalType":"uint256[7]","name":"orderedHistory","type":"uint256[7]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"getStreakTotal","outputs":[{"internalType":"uint24","name":"","type":"uint24"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"feeContract","type":"address"},{"internalType":"address","name":"association","type":"address"},{"internalType":"address","name":"participationToken","type":"address"}],"name":"initialize","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"user","type":"address"}],"name":"isStreakActive","outputs":[{"internalType":"bool","name":"isActive","type":"bool"},{"internalType":"uint256","name":"streakExpiryTimestamp","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"proxiableUUID","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"repairStreak","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"feeContract","type":"address"}],"name":"updateFeeContractAddress","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"participationToken","type":"address"}],"name":"updateParticipationToken","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"}],"name":"upgradeTo","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newImplementation","type":"address"},{"internalType":"bytes","name":"data","type":"bytes"}],"name":"upgradeToAndCall","outputs":[],"stateMutability":"payable","type":"function"}]')

def swapSilverGold(sender, key, amount, targetaddr):
    try:
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender)
        target_contract = web3_hv.to_checksum_address(targetaddr)
        totalamount = int(amount * (10**18))
        func_swap = bytes.fromhex('43604e8a')
        enc_swap = encode(['uint256'], [totalamount])
        rawdata = web3_hv.to_hex(func_swap+enc_swap)
        gasAmount = web3_hv.eth.estimate_gas({
            'chainId': chainId_hv,
            'from': sender,
            'to': target_contract,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        })

        swap_tx = {
            'chainId': chainId_hv,
            'from': sender,
            'to': target_contract,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        }
            
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(swap_tx, key).rawTransaction)
        print(f'Processing Swap Silver Token With Amount Of {amount} To Gold...')
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Swap Silver Token With Amount Of {amount} To Gold Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------') 
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass

def approvalSilver(sender, key, amount, tokenaddr, targetaddr):
    try:
        token_contract = web3_hv.eth.contract(address=web3_hv.to_checksum_address(tokenaddr), abi=token_abi)
        tokenName = token_contract.functions.name().call()
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender)
        unliappv = 2 ** 256 - 1
        gasAmount = token_contract.functions.approve(targetaddr, unliappv).estimate_gas({
            'chainId': chainId_hv,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        appv_tx = token_contract.functions.approve(targetaddr, unliappv).build_transaction({
            'chainId': chainId_hv,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(appv_tx, key).rawTransaction)
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Approval To Address {targetaddr} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
        swapSilverGold(sender, key, amount, targetaddr)
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def approvalSilverCheck():
    try:
        senderkey = input('Input Your Privatekey EVM : ')
        amount = float(input('Input Amount Of Silver Token To Swap : '))
        sender = web3_hv.eth.account.from_key(senderkey)
        target_contract = web3_hv.to_checksum_address('0x7184138c866258f56ca78520951806dda980c4d0')
        token_addr = web3_hv.to_checksum_address('0xEe2c6465A17325aD2818053b1eca9cc896D61325')
        token_contract = web3_hv.eth.contract(address=token_addr, abi=token_abi)
        apprvcheck = token_contract.functions.allowance(sender.address, target_contract).call()
        amounttoken = token_contract.functions.balanceOf(sender.address).call()
        if apprvcheck > amounttoken:
            print(f'Already Approved! Skip Processing Approval...')
            swapSilverGold(sender.address, sender.key, amount, target_contract)    
        else:
            print(f'Processing Approval To Address {target_contract}...')
            approvalSilver(sender.address, sender.key, amount, token_addr, target_contract)
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass

def mintSilver():
    try:
        print('Only Can Mint 500 Silver Token Daily')
        senderkey = input('Input Your Privatekey EVM : ')
        mint = float(input('Input Amount Of Silver Token To Mint : '))
        sender = web3_hv.eth.account.from_key(senderkey)
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender.address)
        target_contract = web3_hv.to_checksum_address('0xEe2c6465A17325aD2818053b1eca9cc896D61325')
        totalmint = int(mint * (10**18))
        func_mint = bytes.fromhex('dbda4657')
        enc_mint = encode(['uint256'], [totalmint])
        rawdata = web3_hv.to_hex(func_mint+enc_mint)
        gasAmount = web3_hv.eth.estimate_gas({
            'chainId': chainId_hv,
            'from': sender.address,
            'to': target_contract,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        })

        mint_tx = {
            'chainId': chainId_hv,
            'from': sender.address,
            'to': target_contract,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        }
            
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(mint_tx, sender.key).rawTransaction)
        print(f'Processing Mint Silver Token With Amount Of {mint}...')
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Mint Silver Token With Amount Of {mint} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass

def mintFlag():
    try:
        senderkey = input('Input Your Privatekey EVM : ')
        idflag = input('Input Your Country Code/ID Flag : ')
        sender = web3_hv.eth.account.from_key(senderkey)
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender.address)
        target_contract = web3_hv.to_checksum_address('0x8C50b7a690d3A528A138229BAFe45690e71d377d')
        func_mint = bytes.fromhex('bab1836a')
        enc_mint = encode(['string'], [idflag])
        rawdata = web3_hv.to_hex(func_mint+enc_mint)
        gasAmount = web3_hv.eth.estimate_gas({
            'chainId': chainId_hv,
            'from': sender.address,
            'to': target_contract,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        })

        mint_tx = {
            'chainId': chainId_hv,
            'from': sender.address,
            'to': target_contract,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        }
            
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(mint_tx, sender.key).rawTransaction)
        print(f'Processing Mint Country Flag With Code : {idflag} ...')
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Mint Country Flag With Code : {idflag} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def increaseLockesH1():
    try:
        print('Make Sure Have esH1 Token To Processing Increase Amount Of Lock')
        senderkey = input('Input Your Privatekey EVM : ')
        amount = float(input('Input Amount Of esH1 Token To Lock : '))
        maxtx = input('How Many Times Do You Want To Make Transactions ? ')
        sender = web3_hv.eth.account.from_key(senderkey)
        gasPrice = 0
        target_contract = web3_hv.to_checksum_address('0xfaF216B9b9FEaD5427352CdA83bCF131957Ff2Ef')
        totalamount = int(amount * (10**18))
        func_increase = bytes.fromhex('5e56b239')
        enc_increase = encode(['uint256', 'address'], [totalamount, web3_hv.to_checksum_address('0x659dc2d3d8b7502ebf580c6632988fed3024b6ae')])
        rawdata = web3_hv.to_hex(func_increase+enc_increase)
        for i in range(0, int(maxtx)):
            nonce = web3_hv.eth.get_transaction_count(sender.address)
            gasAmount = web3_hv.eth.estimate_gas({
                'chainId': chainId_hv,
                'from': sender.address,
                'to': target_contract,
                'gasPrice': gasPrice,
                'data': rawdata,
                'nonce': nonce
            })

            increase_tx = {
                'chainId': chainId_hv,
                'from': sender.address,
                'to': target_contract,
                'gas': gasAmount,
                'gasPrice': gasPrice,
                'data': rawdata,
                'nonce': nonce
            }
                
            #send rawtx
            tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(increase_tx, sender.key).rawTransaction)
            print(f'Processing Increase Lock esH1 Token With Amount {amount} ...')
            transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Increase Lock esH1 Token With Amount {amount} Success!')
            print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
            print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def lockesH1(sender, key, amount, tokenaddr, targetaddr):
    try:
        # Calculate the date 14 days from now
        datenow = datetime.now() + timedelta(days=14)
        # Convert to Unix timestamp
        unix_lock = int(datenow.timestamp())
        gasPrice = 0
        totalamount = int(amount * (10**18))
        nonce = web3_hv.eth.get_transaction_count(sender)
        target_contract = web3_hv.to_checksum_address(targetaddr)
        func_lock = bytes.fromhex('dcb69fbb')
        enc_lock = encode(['uint256', 'uint256', 'address'], [totalamount, unix_lock, tokenaddr])
        rawdata = web3_hv.to_hex(func_lock+enc_lock)
        gasAmount = web3_hv.eth.estimate_gas({
            'chainId': chainId_hv,
            'from': sender,
            'to': target_contract,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        })

        lock_tx = {
            'chainId': chainId_hv,
            'from': sender,
            'to': target_contract,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        }
            
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(lock_tx, key).rawTransaction)
        print(f'Processing Createlock esH1 Token With Amount {amount} ...')
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Createlock esH1 Token With Amount {amount} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def approvalesH1(sender, key, amount, tokenaddr, targetaddr):
    try:
        token_contract = web3_hv.eth.contract(address=web3_hv.to_checksum_address(tokenaddr), abi=token_abi)
        tokenName = token_contract.functions.name().call()
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender)
        unliappv = 2 ** 256 - 1
        gasAmount = token_contract.functions.approve(targetaddr, unliappv).estimate_gas({
            'chainId': chainId_hv,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        appv_tx = token_contract.functions.approve(targetaddr, unliappv).build_transaction({
            'chainId': chainId_hv,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(appv_tx, key).rawTransaction)
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Approval To Address {targetaddr} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
        lockesH1(sender, key, amount, tokenaddr, targetaddr)
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def approvalesH1Check():
    try:
        print('Make Sure Have esH1 Token To Processing Createlock For 2 Week')
        senderkey = input('Input Your Privatekey EVM : ')
        amount = float(input('Input Amount Of esH1 Token To Lock : '))
        sender = web3_hv.eth.account.from_key(senderkey)
        target_contract = web3_hv.to_checksum_address('0xfaf216b9b9fead5427352cda83bcf131957ff2ef')
        token_addr = web3_hv.to_checksum_address('0x659dc2d3d8b7502ebf580c6632988fed3024b6ae')
        token_contract = web3_hv.eth.contract(address=token_addr, abi=token_abi)
        apprvcheck = token_contract.functions.allowance(sender.address, target_contract).call()
        amounttoken = token_contract.functions.balanceOf(sender.address).call()
        if apprvcheck > amounttoken:
            print(f'Already Approved! Skip Processing Approval...')
            lockesH1(sender.address, sender.key, amount, token_addr, target_contract)    
        else:
            print(f'Processing Approval To Address {target_contract}...')
            approvalesH1(sender.address, sender.key, amount, token_addr, target_contract)
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass

def claimFlexible():
    try:
        print('Make Sure Already Staking Native H1 Testnet')
        print('If Already Claim, Please Wait 1 Minutes To Claim Again!')
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3_hv.eth.account.from_key(senderkey)
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender.address)
        target_contract = web3_hv.to_checksum_address('0x277EA07b05Db2879728E491853c278E42bA635f8')
        data = '0x3d18b912'
        gasAmount = web3_hv.eth.estimate_gas({
            'chainId': chainId_hv,
            'from': sender.address,
            'to': target_contract,
            'gasPrice': gasPrice,
            'data': data,
            'nonce': nonce
        })

        stake_tx = {
            'chainId': chainId_hv,
            'from': sender.address,
            'to': target_contract,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': data,
            'nonce': nonce
        }
            
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(stake_tx, sender.key).rawTransaction)
        print(f'Processing Claim Reward Staking Native H1...')
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Claim Reward Staking Native H1 Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass

def stakeFlexible():
    try:
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3_hv.eth.account.from_key(senderkey)
        amount = float(input('Input Of Amount Native H1 To Staking : '))
        maxtx = input('How Many Times Do You Want To Make Transactions ? ')
        gasPrice = 0
        target_contract = web3_hv.to_checksum_address('0x277EA07b05Db2879728E491853c278E42bA635f8')
        send_amount = web3_hv.to_wei(amount, 'ether')
        data = '0xa694fc3a0000000000000000000000000000000000000000000000000000000000000000'
        for i in range(0, int(maxtx)):
            nonce = web3_hv.eth.get_transaction_count(sender.address)
            gasAmount = web3_hv.eth.estimate_gas({
                'chainId': chainId_hv,
                'from': sender.address,
                'to': target_contract,
                'value': send_amount,
                'gasPrice': gasPrice,
                'data': data,
                'nonce': nonce
            })

            stake_tx = {
                'chainId': chainId_hv,
                'from': sender.address,
                'to': target_contract,
                'gas': gasAmount,
                'gasPrice': gasPrice,
                'value': send_amount,
                'data': data,
                'nonce': nonce
            }
            
            #send rawtx
            tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(stake_tx, sender.key).rawTransaction)
            print(f'Processing Staking Native H1 With Amount {amount}...')
            transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Staking Native H1 With Amount {amount} Success!')
            print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
            print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def addLP(sender, key, amount, tokenamount, tokenaddr, lpnftaddr):
    try:
        # senderkey = input('Input Your Privatekey EVM : ')
        # sender = web3_hv.eth.account.from_key(senderkey)
        # amount = float(input('Input Amount Native H1 To Add Liquidity : '))
        # token_addr = input('Input Token Address : ')
        # tokenaddr = web3_hv.to_checksum_address(token_addr)
        # lpnftaddr = web3_hv.to_checksum_address('0xd64255236209a3C96A0CA138A8136DC6117C9BB1')
        lpnft_contract = web3_hv.eth.contract(address=lpnftaddr, abi=lpnft_abi)
        wethaddr = lpnft_contract.functions.WETH9().call()
        gasPrice = 0
        deadline = int(time.time()) + 1000000
        amountsend = web3_hv.to_wei(amount, 'ether')
        amountsendtoken = web3_hv.to_wei(tokenamount, 'ether')
        amount0outmin = web3_hv.to_wei(float(99.5/100) * tokenamount, 'ether')
        amount1outmin = web3_hv.to_wei(float(99.5/100) * amount, 'ether')
        txMint = lpnft_contract.encode_abi(fn_name="mint", args=[(tokenaddr, wethaddr, 500, -887270, 887270, amountsendtoken, amountsend, amount0outmin, amount1outmin, sender, deadline)])
        txrefundETH = lpnft_contract.encode_abi(fn_name="refundETH", args=[])
        txCall = [txMint, txrefundETH]
        nonce = web3_hv.eth.get_transaction_count(sender)
        gasAmount = lpnft_contract.functions.multicall(txCall).estimate_gas({
            'chainId': chainId_hv,
            'from': sender,
            'value': amountsend,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        lp_tx = lpnft_contract.functions.multicall(txCall).build_transaction({
            'chainId': chainId_hv,
            'from': sender,
            'value': amountsend,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(lp_tx, key).rawTransaction)
        print(f'Processing Add Liquidity With Native H1 {amount}...')
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Add Liquidity With Native H1 {amount} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def approvaladdLP(sender, key, amount, tokenamount, tokenaddr, lpnftaddr):
    try:
        token_contract = web3_hv.eth.contract(address=tokenaddr, abi=token_abi)
        tokenName = token_contract.functions.name().call()
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender)
        unliappv = 2 ** 256 - 1
        gasAmount = token_contract.functions.approve(lpnftaddr, unliappv).estimate_gas({
            'chainId': chainId_hv,
            'from': sender,
            'gasPrice': gasPrice,
            'nonce': nonce
        })

        appv_tx = token_contract.functions.approve(lpnftaddr, unliappv).build_transaction({
            'chainId': chainId_hv,
            'from': sender,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'nonce': nonce
        })
        
        #send rawtx
        tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(appv_tx, key).rawTransaction)
        transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Approval To Address {lpnftaddr} Success!')
        print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
        addLP(sender, key, amount, tokenamount, tokenaddr, lpnftaddr)
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def approvaladdLPCheck():
    try:
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3_hv.eth.account.from_key(senderkey)
        amount = float(input('Input Amount Native H1 To Add Liquidity : '))
        tokenamount = float(input('Input Amount Token To Add Liquidity : '))
        tokenaddr = web3_hv.to_checksum_address(input('Input Token Address : '))
        lpnftaddr = web3_hv.to_checksum_address('0xd64255236209a3C96A0CA138A8136DC6117C9BB1')
        token_contract = web3_hv.eth.contract(address=tokenaddr, abi=token_abi)
        apprvcheck = token_contract.functions.allowance(sender, lpnftaddr).call()
        amounttoken = token_contract.functions.balanceOf(sender).call()
        if apprvcheck > amounttoken:
            print(f'Already Approved! Skip Processing Approval...')
            addLP(sender.address, sender.key, amount, tokenamount, tokenaddr, lpnftaddr)    
        else:
            print(f'Processing Approval To Address {lpnftaddr}...')
            approvaladdLP(sender.address, sender.key, amount, tokenamount, tokenaddr, lpnftaddr)
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
# def deployToken():
    # try:
        # print('Deploy Token & Add Liquidity')
        # senderkey = input('Input Your Privatekey EVM : ')
        # sender = web3_hv.eth.account.from_key(senderkey)
        # name = input('Input Token Name [ AirDrop Family IDN ] : ')
        # symbol = input('Input Token Symbol [ ADFMIDN ] : ')
        # supply = int(input('Input Total Token Supply [ 1000000 ] : '))
        # amount = float(input('Input Amount Native H1 To Add Liquidity : '))
        # tokenamount = float(input('Input Amount Token To Add Liquidity : '))
        # gasPrice = 0
        # nonce = web3_hv.eth.get_transaction_count(sender.address)
        # deployed = web3_hv.eth.contract(abi=deploy_abi, bytecode=bytecode)

        # # gasAmount = deployed.constructor(name, symbol, supply).estimate_gas({
            # # 'chainId': chainId_hv,
            # # 'from': sender.address,
            # # 'gasPrice': gasPrice,
            # # 'nonce': nonce
        # # })
        # gasAmount = 100000

        # deploy_tx = deployed.constructor(name, symbol, supply).build_transaction({
            # 'chainId': chainId_hv,
            # 'from': sender.address,
            # 'gas': gasAmount,
            # 'gasPrice': gasPrice,
            # 'nonce': nonce
        # })
        
        # #send rawtx
        # tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(deploy_tx, sender.key).rawTransaction)
        # print(f'Processing Deployed Token...')
        # transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
        # print(f'Deployed {name} Token With Total Supply {supply} Success!')
        # print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
        # print(f'Token Address : {transaction_receipt.contractAddress}')
        # print(f'--------------------------------------------------------------')
        # #approvaladdLPCheck(sender.address, sender.key, amount, tokenamount, transaction_receipt.contractAddress)
    # except Exception as e:
        # print(f"Error: {e}")
        # print(f'')
        # pass
    
def swapBuy():
    try:
        getfee_abi = json.loads('[{"inputs":[],"name":"getFee","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
        getfee_contract = web3_hv.eth.contract(address=web3_hv.to_checksum_address('0xe003BdBa0529ED4E1F2B7f40E4E136904fcaD435'), abi=getfee_abi)
        getfee = getfee_contract.functions.getFee().call()
        print(f'Processing Swap Need Fee Native {getfee / (10**18)} H1')
        print(f'Example If You Swap 0.1 Native H1 Total Will Cost {0.1+getfee / (10**18)}')
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3_hv.eth.account.from_key(senderkey)
        minamount = float(input('Input Min Amount Native H1 To Swap : '))
        maxamount = float(input('Input Max Amount Native H1 To Swap : '))
        token_addr = input('Input Token Address : ')
        tokenaddr = web3_hv.to_checksum_address(token_addr)
        routeraddr = web3_hv.to_checksum_address('0x0dd6D2A8078Fe208B05292D76eaAf9Af0136A212')
        maxtx = input('How Many Times Do You Want To Make Transactions ? ')
        router_contract = web3_hv.eth.contract(address=routeraddr, abi=router_abi)
        token_contract = web3_hv.eth.contract(address=tokenaddr, abi=token_abi)
        tokenName = token_contract.functions.name().call()
        wethaddr = router_contract.functions.WETH().call()
        gasPrice = 0
        deadline = int(time.time()) + 1000000
        random_amount = random.uniform(minamount, maxamount)
        amountsend = web3_hv.to_wei(random_amount, 'ether')
        totalsend = amountsend+getfee
        for i in range(0, int(maxtx)):
            nonce = web3_hv.eth.get_transaction_count(sender.address)
            gasAmount = router_contract.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(0, [wethaddr, tokenaddr], sender.address, deadline).estimate_gas({
                'chainId': chainId_hv,
                'from': sender.address,
                'value': totalsend,
                'gasPrice': gasPrice,
                'nonce': nonce
            })

            swap_tx = router_contract.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(0, [wethaddr, tokenaddr], sender.address, deadline).build_transaction({
                'chainId': chainId_hv,
                'from': sender.address,
                'value': totalsend,
                'gas': gasAmount,
                'gasPrice': gasPrice,
                'nonce': nonce
            })
            
            #send rawtx
            tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(swap_tx, sender.key).rawTransaction)
            print(f'Processing Swap Native {random_amount} To {tokenName} Token...')
            transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Swap Native {random_amount} To {tokenName} Token Success!')
            print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
            print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
    
def sendToken():
    try:
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3.eth.account.from_key(senderkey)
        amounttoken = float(input('Input Of Amount USDT Token To Bridge : '))
        maxtx = input('How Many Times Do You Want To Make Transactions ? ')
        recepient = web3.to_checksum_address('0xDcD8034B880ae80217c3523FBBAB98A68D772156')
        gasPrice = web3.eth.gas_price
        token_contract = web3.eth.contract(address=web3.to_checksum_address('0xbDeaD2A70Fe794D2f97b37EFDE497e68974a296d'), abi=token_abi)
        tokenName = token_contract.functions.name().call()
        tokenDec = token_contract.functions.decimals().call()
        send_amount = int(amounttoken * (10**tokenDec))
        for i in range(0, int(maxtx)):
            nonce = web3.eth.get_transaction_count(sender.address)
            gasAmount = token_contract.functions.transfer(recepient, send_amount).estimate_gas({
                'chainId': chainId,
                'from': sender.address,
                'gasPrice': gasPrice,
                'nonce': nonce
            })

            token_tx = token_contract.functions.transfer(recepient, send_amount).build_transaction({
                'chainId': chainId,
                'from': sender.address,
                'gas': gasAmount,
                'gasPrice': gasPrice,
                'nonce': nonce
            })
            
            #send rawtx
            tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(token_tx, sender.key).rawTransaction)
            print(f'Processing Send {tokenName} Token With Amount {amounttoken} To {recepient}...')
            transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            print(f'Send {tokenName} Token With Amount {amounttoken} To {recepient} Success!')
            print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
            print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass    
        
def mintToken():
    try:
        print('Daily Mint 10 USDT Token Sepolia Testnet')
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3.eth.account.from_key(senderkey)
        gasPrice = web3.eth.gas_price
        target_contract = web3.to_checksum_address('0xbDeaD2A70Fe794D2f97b37EFDE497e68974a296d')
        rawdata = '0x1249c58b'
        nonce = web3.eth.get_transaction_count(sender.address)
        gasAmount = web3.eth.estimate_gas({
            'chainId': chainId,
            'from': sender.address,
            'to': target_contract,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        })

        mint_tx = {
            'chainId': chainId,
            'from': sender.address,
            'to': target_contract,
            'gas': gasAmount,
            'gasPrice': gasPrice,
            'data': rawdata,
            'nonce': nonce
        }
        
        #send rawtx
        tx_hash = web3.eth.send_raw_transaction(web3.eth.account.sign_transaction(mint_tx, sender.key).rawTransaction)
        print(f'Processing Mint 10 USDT Token...')
        transaction_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
        print(f'Mint 10 USDT Token Success!')
        print(f'TX-ID : {str(web3.to_hex(tx_hash))}')
        print(f'--------------------------------------------------------------')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def dailyGM():
    try:
        senderkey = input('Input Your Privatekey EVM : ')
        sender = web3_hv.eth.account.from_key(senderkey)
        gasPrice = 0
        nonce = web3_hv.eth.get_transaction_count(sender.address)
        daily_contract = web3_hv.eth.contract(address=web3_hv.to_checksum_address('0x86e888e3d8179c3d9E4fba15BcEc164C40B7cF37'), abi=daily_abi)
        print(f'GM Streak : {daily_contract.functions.getStreak(sender.address).call()}')
        print(f'Streak Total : {daily_contract.functions.getStreakTotal(sender.address).call()}')
        canContinue = daily_contract.functions.canContinueStreak(sender.address).call()
        if True == canContinue[0]:
            gasAmount = daily_contract.functions.continueStreak().estimate_gas({
                'chainId': chainId_hv,
                'from': sender.address,
                'gasPrice': gasPrice,
                'nonce': nonce
            })

            daily_tx = daily_contract.functions.continueStreak().build_transaction({
                'chainId': chainId_hv,
                'from': sender.address,
                'gasPrice': gasPrice,
                'gas': gasAmount,
                'nonce': nonce
            })
            
            #send rawtx
            tx_hash = web3_hv.eth.send_raw_transaction(web3_hv.eth.account.sign_transaction(daily_tx, sender.key).rawTransaction)
            print(f'Processing GM Daily Onchain...')
            transaction_receipt = web3_hv.eth.wait_for_transaction_receipt(tx_hash)
            print(f'GM Daily Onchain Success!')
            print(f'TX-ID : {str(web3_hv.to_hex(tx_hash))}')
            print(f'--------------------------------------------------------------')
        else:
            print(f'Cannot Continue! Please Wait Until {datetime.fromtimestamp(canContinue[1])}')
    except Exception as e:
        print(f"Error: {e}")
        print(f'')
        pass
        
def menupassport():       
    print('1.) Mint Flag With CountryID H1 Testnet')
    print('2.) Mint Silver Token H1 Testnet')
    print('3.) Swap Silver To Gold Token H1 Testnet')
    choosemenu = input('Choose Menu : ')    
    if str('1') == choosemenu:
        mintFlag()
    elif str('2') == choosemenu:
        mintSilver()
    elif str('3') == choosemenu:
        approvalSilverCheck()
    else:
        print('No Choose Will Exit...')
        exit()
        
def menustakelocked():        
    print('1.) Createlock esH1 Token H1 Testnet')
    print('2.) Increase Lock Amount Of esH1 Token H1 Testnet')
    choosemenu = input('Choose Menu : ')    
    if str('1') == choosemenu:
        approvalesH1Check()  
    elif str('2') == choosemenu:
        increaseLockesH1()
    else:
        print('No Choose Will Exit...')
        exit()

def menustakeflexible():        
    print('1.) Staking Native H1 Testnet')
    print('2.) Claim Reward Staking Native H1 Testnet')
    choosemenu = input('Choose Menu : ')    
    if str('1') == choosemenu:
        stakeFlexible()
    elif str('2') == choosemenu:
        claimFlexible()
    else:
        print('No Choose Will Exit...')
        exit()
        
def menudex():
    print('Coming Soon!')
    # print('1.) Swap Buy Token H1 Testnet')
    # print('2.) Add Liquidity Token Native H1 Testnet')
    # choosemenu = input('Choose Menu : ')    
    # if str('1') == choosemenu:
        # swapBuy()
    # elif str('2') == choosemenu:
        # deployToken()
    # else:
        # print('No Choose Will Exit...')
        # exit()
        
def menusepolia():        
    print('1.) Daily Mint 10 USDT Sepolia Testnet')
    print('2.) Bridge USDT Sepolia To H1 Testnet')
    choosemenu = input('Choose Menu : ')    
    if str('1') == choosemenu:
        mintToken()
    elif str('2') == choosemenu:
        sendToken()
    else:
        print('No Choose Will Exit...')
        exit()

print('0.) GM Daily Onchain')
print('1.) Mint & Bridge USDT Sepolia To Haven1 Testnet')
print('2.) Swap/Add Liquidity hSwap Haven1 Testnet')
print('3.) hStaking Flexible Haven1 Testnet')
print('4.) hStaking Locked Haven1 Testnet')
print('5.) Engage with Haven1 Passport Demo Applications')
choosemenu = input('Choose Menu : ')
if str('0') == choosemenu:
    dailyGM()
elif str('1') == choosemenu:
    menusepolia()
elif str('2') == choosemenu:
    menudex()
elif str('3') == choosemenu:
    menustakeflexible()
elif str('4') == choosemenu:
    menustakelocked()
elif str('5') == choosemenu:
    menupassport()
else:
    print('No Choose Will Exit...')
    exit()
