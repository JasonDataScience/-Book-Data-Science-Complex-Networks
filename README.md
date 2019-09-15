# [Book] Data Science & Complex Networks

## Introduction

This book provides a comprehensive set of describing the basic concept of Complex Network Theory. You are able to find this book at Amazon.com or [Oxford University Press](https://global.oup.com/academic/product/data-science-and-complex-networks-9780199639601?cc=kr&lang=en&), which was written by Guido Caldarelli and Alessandro Chessa. I joined to research this book of [nonce dsrv labs](https://www.dsrvlabs.com/), research lab of cryptoeconomics and blockchain-based network. It spans the topic from food webs to the World-Wide Web, which is also devoted to the definition of the important network models.

You might be able to find the Jupyter Notebook-based code on this [Github Repository](https://github.com/datascienceandcomplexnetworks/book_code).

## Purpose

The aim of this book is to show how network theory is a crucial tool for modeling and filtering the information to readers like me, those who would like to explore from straightforward concepts to more elaborated instruments and quantities. It is to be noted that since the practical situations the data we are interested in are often in a raw and unformatted form, as much very different from we see in lots of textbooks and publications. I would like to start from this point in general form by learning how the basic concepts of complex networks is implemented in plethora of different fields.

## Topics explained

* Chapter 1: foodwebs. Showing how to represent a graphy by means of an adjacency matrix, and introducing concepts related to the property of a single vertex and its neighbours such as the degree and clustering degree sequence.
* Chapter 2: World Trade Web under various aggregations to move to two-vertices properties such as assortativity and reciprocity, and introducing a special kind of graph that is particularly useful for the analysis of social networks, so-called "bipartite graph"
* Chapter 3: Studying the structure of the Internet and introducing various measures of centrality used to assess the robustness of the structure.
* Chapter 4: Studying World Wide Web and Wikipedia, introducing another measure of centrality given by [PageRank](https://lovit.github.io/machine%20learning/2018/04/16/pagerank_and_hits/), introduced by Google in their early days. Then moving onto Wikipedia, as a playing field for the analysis of communities in particular introducing the Girvan-Newman community detection method based on betweenness.
* Chapter 5: Taking into consideration some instances of financial networks, which its dataset allows us to define centrality measures as the [DebtRank](https://arxiv.org/pdf/1504.01857.pdf).

* Chapter 6: Presenting a series of models among which are the random graph model, the configuration model, the gravity model, the fitness model, the Barabasi-Albert model, the copying model, they dynamic fitness models, and a methodology to reconstruct networks from missing information.

## Installation and Preparation

You are expected to have at least Python 3+ with appropriate IDEs including Jupyter Notebook or PyCharm. The book author initialized the code on the operating system of Linux-based, and Mac.

Possibly the Anaconda package is required, including Numpy, Scipy, Matploitlib and NetworkX.

Dependencies are for the libraries: BeautifulSoup, Twython, yahoo_finance, and sympy.

You can find more information on their [website](book.complexnetworks.net).
