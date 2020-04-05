function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta




hypoFunc = sigmoid(X*theta);
jArray = (-1)*(y.*log(hypoFunc)) - (1-y).*log(1-hypoFunc);
J = (1/m) * sum(jArray) + (lambda/(2*m))*sum(theta([2,length(theta)],1).^2);

%Don't regularize the first parameter
grad(1,1) = (1/m) * sum((hypoFunc-y).*X(:,1));

%regularize the rest of the params
thetaLen = length(theta);
for j = 2:thetaLen
    grad(j,1) = (1/m) * sum((hypoFunc-y).*X(:,j)) + (lambda/m)*theta(j);



% =============================================================

end
