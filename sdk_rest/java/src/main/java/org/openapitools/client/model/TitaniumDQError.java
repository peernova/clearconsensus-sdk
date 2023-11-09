/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumDQError
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-09T12:04:47.539075Z[UTC]")
public class TitaniumDQError {
  public static final String SERIALIZED_NAME_CRITERIA_NAME = "criteriaName";
  @SerializedName(SERIALIZED_NAME_CRITERIA_NAME)
  private String criteriaName;

  public static final String SERIALIZED_NAME_ERROR_MESSAGE = "errorMessage";
  @SerializedName(SERIALIZED_NAME_ERROR_MESSAGE)
  private String errorMessage;

  public static final String SERIALIZED_NAME_RULE_NAME = "ruleName";
  @SerializedName(SERIALIZED_NAME_RULE_NAME)
  private String ruleName;

  public static final String SERIALIZED_NAME_RULESET_NAME = "rulesetName";
  @SerializedName(SERIALIZED_NAME_RULESET_NAME)
  private String rulesetName;

  public static final String SERIALIZED_NAME_SEVERITY = "severity";
  @SerializedName(SERIALIZED_NAME_SEVERITY)
  private String severity;

  public TitaniumDQError() { 
  }

  public TitaniumDQError criteriaName(String criteriaName) {
    
    this.criteriaName = criteriaName;
    return this;
  }

   /**
   * Get criteriaName
   * @return criteriaName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getCriteriaName() {
    return criteriaName;
  }


  public void setCriteriaName(String criteriaName) {
    this.criteriaName = criteriaName;
  }


  public TitaniumDQError errorMessage(String errorMessage) {
    
    this.errorMessage = errorMessage;
    return this;
  }

   /**
   * Get errorMessage
   * @return errorMessage
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getErrorMessage() {
    return errorMessage;
  }


  public void setErrorMessage(String errorMessage) {
    this.errorMessage = errorMessage;
  }


  public TitaniumDQError ruleName(String ruleName) {
    
    this.ruleName = ruleName;
    return this;
  }

   /**
   * Get ruleName
   * @return ruleName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getRuleName() {
    return ruleName;
  }


  public void setRuleName(String ruleName) {
    this.ruleName = ruleName;
  }


  public TitaniumDQError rulesetName(String rulesetName) {
    
    this.rulesetName = rulesetName;
    return this;
  }

   /**
   * Get rulesetName
   * @return rulesetName
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getRulesetName() {
    return rulesetName;
  }


  public void setRulesetName(String rulesetName) {
    this.rulesetName = rulesetName;
  }


  public TitaniumDQError severity(String severity) {
    
    this.severity = severity;
    return this;
  }

   /**
   * Get severity
   * @return severity
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getSeverity() {
    return severity;
  }


  public void setSeverity(String severity) {
    this.severity = severity;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumDQError titaniumDQError = (TitaniumDQError) o;
    return Objects.equals(this.criteriaName, titaniumDQError.criteriaName) &&
        Objects.equals(this.errorMessage, titaniumDQError.errorMessage) &&
        Objects.equals(this.ruleName, titaniumDQError.ruleName) &&
        Objects.equals(this.rulesetName, titaniumDQError.rulesetName) &&
        Objects.equals(this.severity, titaniumDQError.severity);
  }

  @Override
  public int hashCode() {
    return Objects.hash(criteriaName, errorMessage, ruleName, rulesetName, severity);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumDQError {\n");
    sb.append("    criteriaName: ").append(toIndentedString(criteriaName)).append("\n");
    sb.append("    errorMessage: ").append(toIndentedString(errorMessage)).append("\n");
    sb.append("    ruleName: ").append(toIndentedString(ruleName)).append("\n");
    sb.append("    rulesetName: ").append(toIndentedString(rulesetName)).append("\n");
    sb.append("    severity: ").append(toIndentedString(severity)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("criteriaName");
    openapiFields.add("errorMessage");
    openapiFields.add("ruleName");
    openapiFields.add("rulesetName");
    openapiFields.add("severity");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumDQError
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumDQError.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumDQError is not found in the empty JSON string", TitaniumDQError.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumDQError.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumDQError` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      if (jsonObj.get("criteriaName") != null && !jsonObj.get("criteriaName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `criteriaName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("criteriaName").toString()));
      }
      if (jsonObj.get("errorMessage") != null && !jsonObj.get("errorMessage").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `errorMessage` to be a primitive type in the JSON string but got `%s`", jsonObj.get("errorMessage").toString()));
      }
      if (jsonObj.get("ruleName") != null && !jsonObj.get("ruleName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `ruleName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("ruleName").toString()));
      }
      if (jsonObj.get("rulesetName") != null && !jsonObj.get("rulesetName").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `rulesetName` to be a primitive type in the JSON string but got `%s`", jsonObj.get("rulesetName").toString()));
      }
      if (jsonObj.get("severity") != null && !jsonObj.get("severity").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `severity` to be a primitive type in the JSON string but got `%s`", jsonObj.get("severity").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumDQError.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumDQError' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumDQError> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumDQError.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumDQError>() {
           @Override
           public void write(JsonWriter out, TitaniumDQError value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumDQError read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumDQError given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumDQError
  * @throws IOException if the JSON string is invalid with respect to TitaniumDQError
  */
  public static TitaniumDQError fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumDQError.class);
  }

 /**
  * Convert an instance of TitaniumDQError to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

